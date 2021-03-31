### ```official_test_v2.csv``` config file   

```
{
    "out_num" : 10000,
    "out_dist":{
        "corrupted" : 0.55,
        "non_corrupted" : 0.3,
        "foreign_random" : 0.1,
        "random" : 0.05
    },
    "input_files": [    "evaluation/data/true_words.txt",
                        "https://github.com/tdd-ai/Spellchecker-Data/blob/main/Data/All/Final/unique%20final.txt" ],
    "input_dist": [ 0.7, 0.15],
    "foreign_file" : "evaluation/data/basic_english_words.csv",
    "out_file" : "evaluation/data/official_test_v2.csv"
}
```