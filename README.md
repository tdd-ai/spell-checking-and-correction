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
| [TurkishSpellChecker](https://github.com/StarlangSoftware/TurkishSpellChecker-Py)                       |   |   |   |   |   |
| [zemberek-nlp](https://github.com/ahmetaa/zemberek-nlp)                                                 |   |   |   |   |   |
| [hunspell-tr](https://github.com/vdemir/hunspell-tr)  (vdemir)                                          | 81.23 | 97.16 | 88.48 | 80.11 | 632.92 |
| [hunspell-tr](https://github.com/hrzafer/hunspell-tr) (hrzafer)                                         |   |   |   |   |   |
| [zemberek-python](https://github.com/Loodos/zemberek-python)                                            |   |   |   |   |   |
| [velhasil](https://github.com/MiniVelhasil/velhasil)                                                    |   |   |   |   |   |
| [tr-spell](https://code.google.com/archive/p/tr-spell/)                                                 |   |   |   |   |   |
| [Turkish-Spell-Checker](https://github.com/tarekwelaya/Turkish-Spell-Checker)                           |   |   |   |   |   |  
