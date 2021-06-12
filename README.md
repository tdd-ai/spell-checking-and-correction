# Spell Checking and Correction

### Todo list:

- [ ] Dataset creation and cleaning  
  - TDK Güncel Türkçe Sözlük
  - Using data from big corpus (OSCAR)
  - ZemberekNLP data
- [x] Data Augmentation script
- [x] Prepare test set
- [x] Evaluate on existing spell checkers
- [ ] Research on creating better .aff/.dic training


### Notes:
- No reply for the developers of [10fastfingers.com](https://10fastfingers.com/typing-test/turkish) ?

### Turkish Spell Checker List

The following table shows the performance of Turkish spell checkers on [official_test.csv](evaluation/data/official_test.csv) dataset.


| Spell Checker | Error detection Precision | Error detection Recall | Error detection F1-Score | Correction accuracy |
| --- | --- | --- | --- | --- |
| [TurkishSpellChecker](https://github.com/StarlangSoftware/TurkishSpellChecker-Py)                       | 94.69 | 39.09 | 55.34 | 60.91 |
| [zemberek-nlp](https://github.com/ahmetaa/zemberek-nlp)                                                 | 99.06 | 94.05 | 96.49 | 99.24 |
| [hunspell-tr](https://github.com/vdemir/hunspell-tr)  (vdemir)                                          | 81.23 | 97.16 | 88.48 | 80.11 |
| [hunspell-tr](https://github.com/hrzafer/hunspell-tr) (hrzafer)                                         | 92.73 | 96.51 | 94.58 | 79.68 |
| [zemberek-python](https://github.com/Loodos/zemberek-python)                                            | 91.07 | 94.42 | 92.71 | 91.61 |
| [velhasil](https://github.com/MiniVelhasil/velhasil)                                                    | 96.77 | 94.19 | 95.46 | 93.92 |
| [tr-spell](https://code.google.com/archive/p/tr-spell/)                                                 | 87.42 | 96.96 | 91.94 | 87.37 |
| [LibraOffice (hr-zafer)](https://github.com/LibreOffice/dictionaries/tree/master/tr_TR)                 | 92.73 | 96.51 | 94.58 | 79.68 |
| [Ours_v1]()                                                                                             | 96.63 | 94.21 | 95.40 | 96.44  |
| [Ours_v2]()                                                                                             | 97.23 | 94.38 | 95.78 | 97.15  |

The following table shows the performance of Turkish spell checkers on [official_test_v2.csv](evaluation/data/official_test_v2.csv) dataset.


| Spell Checker | Error detection Precision | Error detection Recall | Error detection F1-Score | Correction accuracy |
| --- | --- | --- | --- | --- |
| [TurkishSpellChecker](https://github.com/StarlangSoftware/TurkishSpellChecker-Py)                       | 96.54 | 63.91 | 76.91 | 36.09 |
| [zemberek-nlp](https://github.com/ahmetaa/zemberek-nlp)                                                 | 97.83 | 87.75 | 92.52 | 63.52 |
| [hunspell-tr](https://github.com/vdemir/hunspell-tr)  (vdemir)                                          | 90.96 | 97.47 | 94.10 | 48.41 |
| [hunspell-tr](https://github.com/hrzafer/hunspell-tr) (hrzafer)                                         | 95.38 | 97.27 | 96.32 | 48.93 |
| [zemberek-python](https://github.com/Loodos/zemberek-python)                                            | 96.62 | 96.05 | 96.33 | 53.84 |
| [velhasil](https://github.com/MiniVelhasil/velhasil)                                                    | 96.74 | 94.73 | 95.73 | 52.99 |
| [tr-spell](https://code.google.com/archive/p/tr-spell/)                                                 | 93.66 | 97.24 | 95.42 | 54.65 |
| [LibraOffice (hr-zafer)](https://github.com/LibreOffice/dictionaries/tree/master/tr_TR)                 | 95.38 | 97.27 | 96.32 | 48.93 | 
| [Ours_v1]()                                                                                             | 97.70 | 94.69 | 96.17 | 55.80  |
| [Ours_v2]()                                                                                             | 97.85 | 95.25 | 96.53 | 56.38  |
