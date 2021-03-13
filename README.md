# Spell Checking and Correction

### Todo list:

- [ ] Dataset creation and cleaning  
  - TDK Güncel Türkçe Sözlük
  - Using data from big corpus (OSCAR)
  - ZemberekNLP data
- [x] Data Augmentation script
- [x] Prepare test set
- [ ] Evaluate on existing spell checkers
- [ ] Research on creating better .aff/.dic training


### Notes:
- No reply for the developers of [10fastfingers.com](https://10fastfingers.com/typing-test/turkish) ?

### Turkish Spell Checker List

The following table shows the performance of Turkish spell checkers on [official_test.csv](evaluation/data/official_test.csv) dataset.


| Spell Checker | Error detection Precision | Error detection Recall | Error detection F1-Score | Correction accuracy | Speed (words per sec) |
| --- | --- | --- | --- | --- | --- |
| [TurkishSpellChecker](https://github.com/StarlangSoftware/TurkishSpellChecker-Py)                       |  94.69 |  39.09 |  55.34 |  60.91 | 1.06  |
| [zemberek-nlp](https://github.com/ahmetaa/zemberek-nlp)                                                 |  99.06 |  94.05 | 96.49  | 99.24  | 397.65  |
| [hunspell-tr](https://github.com/vdemir/hunspell-tr)  (vdemir)                                          | 81.23 | 97.16 | 88.48 | 80.11 | 632.92 |
| [hunspell-tr](https://github.com/hrzafer/hunspell-tr) (hrzafer)                                         |  92.73 |  96.51 | 94.58  | 79.68  |  4.50 |
| [zemberek-python](https://github.com/Loodos/zemberek-python)                                            |  91.07 | 94.42  |  92.71 | 91.61 |  18.70 |
| [velhasil](https://github.com/MiniVelhasil/velhasil)                                                    |   |   |   |   |   |
| [tr-spell](https://code.google.com/archive/p/tr-spell/)                                                 | 87.42 | 96.96 | 91.94 | 87.37 |  3.24 |
| [Turkish-Spell-Checker](https://github.com/tarekwelaya/Turkish-Spell-Checker)                           |   |   |   |   |   |  
