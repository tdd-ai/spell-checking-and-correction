# Spell Checker Evaluation

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

```
Error Correction Accuracy = 80.11
```

## Evaluation script

`evaluate.py` script

The format of input is jsonlines, there is an input sample in [eval_input_sample.json](eval_input_sample.json).

- spelling: 1 if there is an error, 0 if the spelling of "input" is correct.
- suggestions: this will be evaluated only if the "input" is not the same as "gold".

One word example per line:

```json
{
  "input": "tipisiniz",
  "gold": "tipisiniz",
  "spelling": 1, 
  "suggestions": [ 
    "tipsiniz",
    "tip isiniz",
    "tip-isiniz",
    "tipi siniz",
    "tipi-siniz",
    "esintisiz",
    "silintisiz"
  ]
}
```

### Script usage

```shell
$ python evaluate.py --input-file eval_input_sample.json

Error Detection Scores:
        Precision = 78.57
        Recall = 100.00
        F1-Score = 88.00

Error Correction Accuracy = 90.91
```
