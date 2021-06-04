import math 
import sys
from tqdm import tqdm
import codecs
from file_hunspell import *

def read_file( filename ):
    f = codecs.open( filename , "r" )
    words = f.readlines()
    words = [ w.rsplit()[0]  for w in words ]
    
    #print("words")
    #print(words)
    
    return words

filename = sys.argv[1]
out_filename = sys.argv[2]

words = read_file( filename )
words = set(words)
words = list(words)
words.sort()


total_prefix_count = {}
total_affix_count = {}


for word in words:
    for i in range( len(word) + 1 ):
        prefix = word[ :i ]
        affix  = word[ i: ]

        if prefix in total_prefix_count.keys():
            total_prefix_count[ prefix ] += 1
        else:
            total_prefix_count[ prefix ] = 1

        if affix in total_affix_count.keys():
            total_affix_count[ affix ] += 1
        else:
            total_affix_count[ affix ] = 1

#print( "total prefix count" )
#print( total_prefix_count )

matches = {}

for word in words:
    u = 0
    
    for i in range( len(word) + 1 ):
        prefix = word[ :i ]
        affix  = word[ i: ]        
        
        cur_u = min( total_prefix_count[prefix] , total_affix_count[affix] )
        
        if cur_u >= u:
            u = cur_u
            best_i = i
            best_prefix = prefix
            best_affix = affix
    
    if best_prefix in matches.keys():
        matches[ best_prefix ] = matches[ best_prefix ].union( {best_affix} )
    else:
        matches[ best_prefix ] = set( best_affix )


#print( matches )
    

#for key in matches.keys():
#    for a in matches[key]:
#        print(a)

#print( "matches:\n", matches. )

create_hunspell_files( matches, out_filename )

