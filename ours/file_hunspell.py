from tqdm import tqdm

def create_hunspell_files( matches, filename ):

   

    matches = clear_matches( matches )


    new_wordlist = []

    affixes = set()
    print( "creating affixes set")
    for k in tqdm( matches.keys() ):
        for a in matches[k]:
            new_wordlist.append( k + a )
            if a != '':
                affixes = affixes.union( {a} )

    i=0
    affixes_dict = {}
    for a in affixes:
        affixes_dict[ a ] = i
        i += 1

    #print("affixes dict :\n", affixes_dict )

    f = open( filename + '.dic' , "a")
    f.write( str( len( matches.keys() ) ) + '\n' )

    print( "creating dic file")
    for k in  tqdm( enumerate( matches.keys() ) ):
        f.write( k )
        
        if(  len(matches[k]) == 0 ):
            f.write('\n')

        if( len(matches[k]) > 0  ):

            if len( matches[k] ) == 1 and '' in matches[k]:
                f.write('\n')
            else:
                f.write('/')

        for j,a in enumerate( matches[k] ):
            if a != '':
                if j != len( matches[k] )-1:
                    f.write( str(affixes_dict[a]) + ',' )
                else:
                    f.write( str(affixes_dict[a]) + '\n' )

                new_wordlist.append( k + a )
                affixes = affixes.union( {a} )

    f.close()

    f = open( filename + '.aff' , "a")

    f.write("LANG tr_TR\nSET UTF-8\nTRY İiIıŞşÇçĞğÜüÖö-qwertyuopasdfghjklzxcvbnmQWERTYUOPASDFGHJKLZXCVBNM'\nFLAG num\n\n")
    print("creating aff file")
    for i,a in tqdm( enumerate( affixes_dict.keys() ) ):
        f.write("SFX " + str( affixes_dict[a] ) + " N 1\n" )
        f.write("SFX " + str( affixes_dict[a] ) + " 0 " + a + " .\n\n" )

    f.close()

    print( "roots length : " ,  len( matches.keys() ) )
    print( "affixes length : ", len( affixes ) )
    

def clear_matches( matches ):

    #print( "matches: " , matches.keys() )

    for key in matches.keys():
        matches[key] = matches[key].difference( {''} )

    return matches