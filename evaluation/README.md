# Evaluation

The evaluation is composed of two parts: 

### Error detection evaluation

Here we evaluate the spelling error detection ability of the spell-checker, as a binary classification problem, and report the precision, recall, and F1 score.


example:

```
Error Detection Scores:

        Precision = 81.23
        Recall = 97.17
        F1-Score = 88.49
```


### Error correction ability

Given the wrong spelled words, we measure the accuracy of the suggestions by the spell-checker.

Error Correction Accuracy = 80.11


### `evaluate.py`

```shell
$ python evaluate.py --input-file eval_input_sample.json

Error Detection Scores:
        Precision = 78.57
        Recall = 100.00
        F1-Score = 88.00

Error Correction Accuracy = 90.91
```
