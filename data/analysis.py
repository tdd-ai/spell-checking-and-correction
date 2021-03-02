from zemberek import TurkishMorphology
from tqdm import tqdm
import sys
import random

REPEATS = [i*3 for i in "a,b,c,ç,d,e,f,g,ğ,h,i,ı,j,k,l,m,n,o,ö,p,r,s,ş,t,u,ü,v,y,z".split(",")]
PUNCTUATIONS = "!#$%&'()*+, -./:;<=>?@[\]^_`{|}~"
ALPHABET = "abcçdefgğhiıjklmnoöprsştuüvyz"

def is_valid(word):
    return (not any(char.isdigit() for char in word)) and (len(word) > 1) \
        and (not word.startswith("ğ")) and (not any(i in word for i in REPEATS)) \
        and (not any(i in word for i in PUNCTUATIONS)) and (not any(len(word) == word.count(i) for i in ALPHABET))


if __name__ == '__main__':
    morphology = TurkishMorphology.create_with_defaults()

    vocab = open(sys.argv[1])
    content = vocab.read()
    content = content.split("\n")

    unique_words = set()
    freq_list = dict()

    for i in tqdm(content):
        if not is_valid(i):
            continue
        result = morphology.analyze(i).analysis_results
        if result:
            stem = result[0].get_stem()
            unique_words.add(stem)
            freq_list[stem] = freq_list.get(stem, 0) + 1

    unique_out = open(sys.argv[2], "w", encoding='utf-8')

    for i in unique_words:
        unique_out.write(str(i)+"\n")

    freq_out = open(sys.argv[3], "w", encoding='utf-8')

    for i in freq_list.items():
        freq_out.write(str(i[0]) + ":" + str(i[1]) + "\n")