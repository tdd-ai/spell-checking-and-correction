# Data
Word curation was made with the following rules : 
a word
- cannot start with ğ
- cannot include a character consecutively 3 times
- cannot include a digit
- its length must be greater than 1
- can be stemmed via zemberek-python
- cannot include punctuation marks
- cannot be consisting of the same characters

**Vocab.all file number of words : 7,755,119**
(unique_vocaball.txt, freq_vocaball.txt)

**zemberek-parsed-words-min10 : 818,47**
(unique_zemberek-parsed-words-min10.txt ,freq_zemberek-parsed-words-min10.txt)

**oflazer-parsed-words : 3,472,887**
(unique_oflazer-parsed-words.txt, freq_oflazer-parsed-words.txt)

**tr-dictionary : 70,626**
(unique_tr-dictionary.txt, freq_tr-dictionary.txt)

**zemberek data = vocab.all + zemberek-parsed-words-min10.txt + oflazer-parsed-words.txt
tdk = tr-dictionary.txt**

**zemberek-intersection : 23,208**
(zemberek-data-intersection.txt)

**zemberek-union : 62,056**
(zemberek-data-union.txt)

**zemberek data- tdk intersection :17,264**
(zemberek-tdk-intersection.txt)

**zemberek data- tdk union : 62,915**
(zemberek-tdk-union.txt)

