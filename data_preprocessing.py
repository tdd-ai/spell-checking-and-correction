import csv
import re
import math
import random
import numpy as np
import sys
import argparse
from tqdm import tqdm
import json

class DataProcessing():
    
    def __init__(self):

        self.keyboard = [   ['q','w','e','r','t','y','u','ı','o','p','ğ','ü'],
                            ['a','s','d','f','g','h','j','k','l','ş','i'],
                            ['z','x','c','v','b','n','m','ö','ç'] ]
        
        self.flat_keyboard = []
        for row in self.keyboard:
            for c in row:
                self.flat_keyboard.append(c)
        
        self.turkish_alphabet = 'abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
        self.ascii_turkish_alphabet = 'abccdefgghiijklmnooprsstuuvyzABCCDEFGGHIIJKLMNOOPRSSTUUVYZ'
        self.ascii_mapping = {}

        for i in range( len(self.turkish_alphabet) ):
            self.ascii_mapping[ self.turkish_alphabet[i] ] = self.ascii_turkish_alphabet[i]

        self.locations = self.get_locations()
        self.replacement_matrix =  self.get_replacement_matrix()

        self.corruption_methods = ["delete","insert","substitude","ascify"]
        self.corruption_weights = [1,1,1,3]
        self.generation_methods = ["foreign_lang","random"]
        
    def get_locations(self):
        locations = {}
        for i,row in enumerate(self.keyboard):
            for j,col in enumerate( row):
                locations[ self.keyboard[i][j] ] = (i,j)

        return locations
        
    def get_replacement_matrix( self ):

        length = len( self.flat_keyboard )
        distance_matrix = np.zeros( (length,length) )
        
        for i1,c1 in enumerate(self.flat_keyboard):
            for i2,c2 in enumerate(self.flat_keyboard):
                x1,y1 = self.locations[c1]
                x2,y2 = self.locations[c2]
                distance_matrix[i1][i2] = abs(x1-x2) + abs(y1-y2)

        #define the weight for each distance probability
        #ex. weights[1] = 10 and weights[2] = 2 means that distance=1 is 5 times more probable than distance=2
        weights = [0,13,2,1]

        replacement_matrix = distance_matrix
        replacement_matrix[ replacement_matrix >= len(weights) ] = 0
        
        for i,w in enumerate(weights):
            replacement_matrix[ distance_matrix==i ] = w

        for row in replacement_matrix:
            row /= np.sum(row)

        return replacement_matrix

    ## Following methods corrupt words or produce non-turkish words.

    def insert_char( self,  word ):
        word = [c for c in word]
        pos = random.randint(0, len(word) - 1)
        c = word[pos]
        insert_char = np.random.choice( self.flat_keyboard, p=self.replacement_matrix[self.flat_keyboard.index(c)] )
        word.insert( pos , insert_char )
        return ''.join(word)

    def delete_char( self, word ):
        word = [c for c in word]
        pos = random.randint(0, len(word) - 1 )
        del word[pos]
        return ''.join(word)

    def substitude_char( self, word ):
        word = [c for c in word]
        pos = random.randint(0, len(word) - 1 )
        c = word[pos]
        substitude_char = np.random.choice( self.flat_keyboard, p=self.replacement_matrix[self.flat_keyboard.index(c)] )
        word[pos] = substitude_char
        return ''.join(word)

    def all_ascii( self, word):
        return all(ord(c) < 128 for c in word)
        '''
        for c in word:
            if c not in self.ascii_turkish_alphabet:
                return False 
        return True
        '''

    def asciify_char( self, word ):
        word = [c for c in word]
        non_asciis = [ i  for i,c in enumerate(word) if ord(c) >= 128  ]
        pos = random.choice( non_asciis )
        #print("ascified word : ", word, " pos : " , pos)
        substitude_char = random.choice( self.ascii_mapping[ word[pos] ] )
        word[pos] = substitude_char
        return ''.join(word)

    def random_word( self ):
        length = random.choice( [4,5,6] )
        chars = [ c for c in self.turkish_alphabet ]
        word = [ random.choice(chars) for _ in range(length) ]
        return ''.join(word)

    def import_foreign_words(self, filename):
        f = open( filename, "r")
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]

        self.foreign_words = []
        non_turkish = ['q','w','x']

        for word in lines:
            if word.isalpha() and ( len(word) > 4 or any( nt in word for nt in non_turkish )  ):
                self.foreign_words.append( word )

        
    def random_foreign_word( self ):
        fword =  random.choice( self.foreign_words )    
        fword = [c for c in fword]
        fword[0] = fword[0].upper()
        return ''.join(fword)        

    def random_corruption_method( self, word ):
        methods = self.corruption_methods
        weights = np.array( self.corruption_weights )
        if len(word) == 1: #strings of lenth 1 should not be deleted
            methods = methods[1:]
            weights = weights[1:]
        if self.all_ascii(word): #all ascii strings should not be asciified
            methods = methods[:-1]
            weights = weights[:-1]


        weights = [w/np.sum(weights) for w in weights ]
        method = np.random.choice( methods, p=weights )
        return method


    def corrupt_word(self, word ):
        num_corruptions = 1
        if len(word) > 4:
            num_corruptions = np.random.choice( [1,2,3] , p = [0.7,0.25,0.05] )    

        corrupted_word = word
        for _ in range(num_corruptions):
            method = self.random_corruption_method(corrupted_word)
            if method == 'delete':
                corrupted_word = self.delete_char( corrupted_word )
            elif method == 'insert':
                corrupted_word = self.insert_char( corrupted_word )
            elif method == 'substitude':
                corrupted_word = self.substitude_char( corrupted_word )
            elif method == 'ascify':
                corrupted_word = self.asciify_char( corrupted_word )

        return corrupted_word

    def corrupt_words( self, words , n = 5 ):
        corrupts = []

        for word in tqdm(words):
            corrupts.append( self.corrupt_word(word) )

        return corrupts

'''
Usage :
$python --input-file <INPUT_FILE> --out-file <OUTPUT_FILE>
$python --input-file <INPUT_FILE> --out-file <OUTPUT_FILE> --foreign-file <FOREIGN_WORDS_FILE>
'''

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    
    '''
    parser.add_argument("--input-file", type=str, required=True)
    parser.add_argument("--out-file", type=str, required=True)
    parser.add_argument("--foreign-file", type=str )
    '''
    
    parser.add_argument("--config-file", type=str, required=True)
    args = parser.parse_args()
    

    with open( args.config_file ) as json_data_file:
        data = json.load(json_data_file)

    #print(data)
    word_distirbution = data["out_dist"]

    
    #word_distirbution = {"random":0.05,"foreign_random":0.10,"corrupted":0.5,"non-corrupted":0.35}

    input_filenames = data["input_files"]
    input_dist = data["input_dist"]

    input_num = ( data["out_dist"]["corrupted"] + data["out_dist"]["non_corrupted"] )*data["out_num"]
    
    words = []
    for i,name in enumerate(input_filenames):
        f = open(name,'r') 
        lines = f.readlines()
        w = [word.rstrip() for word in lines ]
        w = random.choices( w , k = int(input_dist[i]*input_num) )
        words.extend( w )

    '''
    f = open(args.input_file, 'r')
    lines = f.readlines()
    words = [word.rstrip() for word in lines ]
    '''
    
    processor = DataProcessing()
    out_size = data["out_num"]

    foreign_filename = data["foreign_file"]
    if foreign_filename is not None and foreign_filename != "":
        processor.import_foreign_words( foreign_filename )

    #Corrupt given input list
    #corrupted_words = processor.corrupt_words( words )

    #corrupted words
    ids = np.arange( len(words) )
    corrupted_ids = np.random.choice(ids, int( out_size*word_distirbution['corrupted'] ),replace=False)

    #non-corrupted words
    non_corrupted_ids = np.random.choice(ids, int( out_size*word_distirbution['non_corrupted'] ),replace=False)

    print("prepearing corrupted words...")
    corrupted_words = [ processor.corrupt_word( words[i] ) for i in tqdm(corrupted_ids) ]

    #Produce random words
    print("prepearing random words...")
    random_words = []
    for _ in tqdm( range( int( out_size*word_distirbution['random'] ) ) ):
        random_words.append( processor.random_word() )

    #Produce random foreign words
    random_foreign_words = []
    if foreign_filename is not None and foreign_filename != "":
        print("prepearing foreign words")
        for _ in tqdm( range( int( out_size*word_distirbution['foreign_random'] ) ) ):
            random_foreign_words.append( processor.random_foreign_word() )

    #Write created words to file
    out_file = open( data["out_file"] , "w")
    out_file.write( 'gold,input\n' )

    for i,id in enumerate(corrupted_ids):
        out_file.write( words[id] + ',' + corrupted_words[i]  + '\n' )

    for id in non_corrupted_ids:
        out_file.write( words[id] + ',' + words[id] +  '\n' )

    for word in random_foreign_words:
        out_file.write( word + ',' + '\n' )

    for word in random_words:
        out_file.write( word + ',' + '\n' )
    
    out_file.close()
    