import csv
import re
import math
import random
import numpy as np
import sys



class DataProcessing():
    
    def __init__(self):
        self.keyboard_cartesian = {'q': {'x': 1, 'y': 1}, 'w': {'x': 2, 'y': 1}, 'e': {'x': 3, 'y': 1},
                                   'r': {'x': 4, 'y': 1}, 't': {'x': 5, 'y': 1}, 'y': {'x': 6, 'y': 1},
                                   'u': {'x': 7, 'y': 1}, 'ı': {'x': 8, 'y': 1}, 'o': {'x': 9, 'y': 1},
                                   'p': {'x':10, 'y': 1}, 'ğ': {'x':11, 'y': 1}, 'ü': {'x':12, 'y': 1},
                                   'a': {'x': 1, 'y': 2}, 's': {'x': 2, 'y': 2}, 'd': {'x': 3, 'y': 2},
                                   'f': {'x': 4, 'y': 2}, 'g': {'x': 5, 'y': 2}, 'h': {'x': 6, 'y': 2},
                                   'j': {'x': 7, 'y': 2}, 'k': {'x': 8, 'y': 2}, 'l': {'x': 9, 'y': 2},
                                   'ş': {'x':10, 'y': 2}, 'i': {'x':11, 'y': 2},
                                   'z': {'x': 1, 'y': 3}, 'x': {'x': 2, 'y': 3}, 'c': {'x': 3, 'y': 3},
                                   'v': {'x': 4, 'y': 3}, 'b': {'x': 5, 'y': 3}, 'n': {'x': 6, 'y': 3},
                                   'm': {'x': 7, 'y': 3}, 'ö': {'x': 8, 'y': 3}, 'ç': {'x': 9, 'y': 3}}
        
        self.nearest_to_i = self.get_nearest_to_i()

    def get_nearest_to_i(self):
        nearest_to_i = {}
        for i in self.keyboard_cartesian.keys():
            nearest_to_i[i] = []
            for j in self.keyboard_cartesian.keys():
                distance = self.euclidean_distance(i, j) 
                if distance < 2.0:
                    nearest_to_i[i].append(j)
        return nearest_to_i


    def euclidean_distance(self, a, b):
        dx = (self.keyboard_cartesian[a]['x'] - self.keyboard_cartesian[b]['x']) ** 2      
        dy = (self.keyboard_cartesian[a]['y'] - self.keyboard_cartesian[b]['y']) ** 2
        return math.sqrt(dx + dy)

    def find_space(self, s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]

    def insert_char( self,  word ):
        word = [c for c in word]
        pos = random.randint(0, len(word) - 1)
        insert_char = random.choice( self.nearest_to_i[ word[pos] ] )
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
        substitude_char = random.choice( self.nearest_to_i[ word[pos] ] )
        word[pos] = substitude_char
        return ''.join(word)

    def corrupt_word(self, word, n = 5 ):
        corrupted_words = []
        for i in range(n):

            if len(word) > 1:
                method = random.randint(1,3)
            else:
                method = random.randint(1,2)
            if method == 1: #insert char
                corrupted_word = self.insert_char( word )
            elif method == 2: # delete char
                corrupted_word = self.substitude_char( word )
            else:
                corrupted_word = self.delete_char( word )

            corrupted_words.append( corrupted_word )

        return corrupted_words

    def corrupt_words( self, words , n = 5 ):
        corrupts = {}

        for word in words:
            corrupts[ word ] = self.corrupt_word( word )

        return corrupts

'''
Usage :
$python <INPUT_FILE> <OUTPUT_FILE>
'''
if __name__ == "__main__":

    filename = sys.argv[1]
    f = open(filename, 'r')
    lines = f.readlines()
    words = [word.rstrip() for word in lines ]

    processor = DataProcessing()
    corrupted_words = processor.corrupt_words( words )

    out_filename = sys.argv[2]
    out_file = open( out_filename , "w")
    
    for key in corrupted_words.keys():
        for cword in corrupted_words[key]:
            out_file.write( key + ',' + cword + '\n' )
    
    out_file.close()
    
    