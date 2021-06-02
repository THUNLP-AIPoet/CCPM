import sys
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score, roc_auc_score
import jsonlines
import numpy as np

def open_file(fn):
    with jsonlines.open(fn) as reader:
        try:
            return [ele for ele in reader]
        except KeyError:
            return

def eval_files():
    if len(sys.argv) != 3:
        return -2, []
    prediction_file = open_file(sys.argv[1])
    test_file = open_file(sys.argv[2])
    if prediction_file is None or test_file is None:
        return -2, []
    if len(prediction_file) != len(test_file):
        return -1, []
    preds, trues = [], []
    for i in range(len(test_file)):
        if 'answer' not in prediction_file[i] or not 0 <= prediction_file[i]['answer'] <= 3:
            return -1, []
        preds.append(prediction_file[i]['answer'])
        trues.append(test_file[i]['answer'])
    preds, trues = np.array(preds), np.array(trues)
    return 0, {
        'precision': precision_score(trues, preds, average='macro'),
        'recall': recall_score(trues, preds, average='macro'),
        'f-1': f1_score(trues, preds, average='macro'),
        'accuracy': accuracy_score(trues, preds),
    }


if __name__ == '__main__':
    info, res = eval_files()
    if info == -2:
        print('File Error')
    elif info == -1:
        print('Prediction File Format Error')
    else:
        print(res)