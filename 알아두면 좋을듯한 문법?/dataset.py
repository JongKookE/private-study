import pandas as pd
import os
import shutil

train_csv = pd.read_csv("/home/jongkook/문서/jk_Ai/code/handpose/train.csv")
train_csv['label'][train_csv['label'] == '10-1'] = 10 ## label : 10-1 -> 10
train_csv['label'][train_csv['label'] == '10-2'] = 0 ## Label : 10-2 -> 0


train_csv.index = train_csv.index + 1
label_index=train_csv.index[train_csv["label"]==0].tolist()
print("드디어 데이터를 알맞게 옮겼어!!!", label_index)

for root, subdirs, files in os.walk("/home/jongkook/문서/jk_Ai/code/handpose/train"):
    for i in range(len(label_index)):
        int_label = str(label_index[i]) + ".png"
        int_label = int_label.zfill(7)
        for f in files:
            if int_label == f:
                file_to_move = os.path.join(root, f)
                shutil.move(file_to_move, "/home/jongkook/문서/jk_Ai/code/hand_classes/0")
