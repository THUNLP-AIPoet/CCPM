# CCPM-MC
### 简介
中国古典诗歌翻译数据集（Chinese Classical Poetry Matching Dataset-Multiple Choice），给定中国古典诗歌的现代文翻译，要求从四句诗中挑选出这句现代文翻译对应的那一句诗歌。
### 数据规模
训练集: 21,778，验证集: 2,720，测试集: 2,720
### 数据格式描述
每条数据包含诗歌对应的翻译(translation，以字符串形式存储)，四个对应诗歌的备选选项(choice，以列表形式存储)，答案编号(answer，为0-3之间的整数)
### 数据样例
{"translation": "一生当中疾病缠身今日独上高台。",

 "choices": ["一春多病几登台", "百年多病独登台", "百年多病负登临", "况多愁病独登台"],

 "answer": 1}