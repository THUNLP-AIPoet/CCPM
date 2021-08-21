# CCPM
[中文](#简介) | [English](#Introduction)

### 简介
中国古典诗歌匹配数据集（Chinese Classical Poetry Matching Dataset），给定中国古典诗歌的现代问描述，要求从候选的四句诗中选出与现代文描述语义匹配的那一句。我们利用古典诗歌和现代文翻译的平行语料构建正确选项，并利用正确选项从古代诗歌语料库中利用相似检索构造出错误候选。

### 数据规模
训练集: 21,778句，验证集: 2,720句，测试集: 2,720句
### 数据格式
每条数据包含诗歌对应的描述(translation，以字符串形式存储)，四个候选诗句(choice，以列表形式存储)，正确诗句的答案编号(answer，为0-3之间的整数)

样例如下：

```
{"translation": "一生当中疾病缠身今日独上高台。",
 "choices": ["一春多病几登台", "百年多病独登台", "百年多病负登临", "况多愁病独登台"],
 "answer": 1}
```
### 评测代码使用

**预测结果需要和训练集数据格式保持一致**

**正确提交文件名：CCPM.jsonl**

```shell
python eval.py prediction_file test_private_file
```

评测指标为Accuracy，输出结果为字典格式：

```python
return 0, {
        'accuracy': accuracy_score(trues, preds),
    }
```

### 引用

如果您使用了本数据集，请引用以下技术报告：
```
@article{li2021CCPM,
  title = {CCPM: A Chinese Classical Poetry Matching Dataset},
  author = {Li, Wenhao and Qi, Fanchao and Sun, Maosong and Yi, Xiaoyuan and Zhang, Jiarui},
  journal={arXiv preprint arXiv:2106.01979},
  year = {2021}
}
```



------

### Introduction

CCPM is a large Chinese classical poetry matching dataset that can be used for poetry matching, understanding and translation. 

The main task of this dataset is: given a description in modern Chinese, the model is supposed to select one line of Chinese classical poetry from four candidates that semantically match the given description most. To construct this dataset, we first obtain a set of parallel data of Chinese classical poetry and modern Chinese translation. Then we retrieve similar lines of poetry with the lines in a poetry corpus as negative choices.

### Size
It contains 27,218 instances in total, which are split into training (21,778 instances), validation (2,720 instances) and test (2,720 instances) sets.

### Format

Each instance is composed of `translation` (the description in modern Chinese, a string), `choice` (four candidate lines of Chinese classical poetry, a list)  and `answer` (the index of the correct line, an integer between 0 and 3).

Here is an example:
```
{"translation": "一生当中疾病缠身今日独上高台。",
 "choices": ["一春多病几登台", "百年多病独登台", "百年多病负登临", "况多愁病独登台"],
 "answer": 1}
```

### Usage of the Evaluation Code

**The format of the prediction file needs to be consistent with the training set.**

**Valid prediction file name：CCPM.jsonl**

```shell
python eval.py prediction_file test_private_file
```

The Evaluation Metric is accuracy, the format of the output is a dictionary as folliowing:\

```python
return {
        'accuracy': accuracy_score(trues, preds),
    }
```

### Citation

Please cite our technical report if you use this dataset:

```
@article{li2021CCPM,
  title = {CCPM: A Chinese Classical Poetry Matching Dataset},
  author = {Li, Wenhao and Qi, Fanchao and Sun, Maosong and Yi, Xiaoyuan and Zhang, Jiarui},
  journal={arXiv preprint arXiv:2106.01979},
  year = {2021}
}
```