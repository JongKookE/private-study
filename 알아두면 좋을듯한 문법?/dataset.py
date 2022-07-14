import pandas as pd
import os
import shutil

train_csv = pd.read_csv("/home/jongkook/문서/jk_Ai/code/handpose/train.csv")

for num_str in range(len(train_csv)):
    train_csv['label'][train_csv['label'] == '10-1'] = 10
    train_csv['label'][train_csv['label'] == '10-2'] = 0
    train_csv['label'][train_csv['label'] == str(num_str)] = num_str
    
for label_idx in range(11):
    globals()["var_{}".format(label_idx)] = train_csv.index[train_csv["label"]==label_idx].tolist()

def hand_classes(label_index, dest):
    for root, subdir, files in os.walk("/home/jongkook/jongkookE/data/train_1"): # root, subdirs, files은 변수가 아닌 실제 경로 안의 루트, 파일 서브 디렉토리를 의미
        for i in range(len(label_index)):
            int_label = str(label_index[i]) + ".png" # 나는 인덱스의 숫자를 파일명의 label과 맞추었기 때문에 추가적으로 인덱스 값 뒤에 ".png"를 넣는 추가 작업이 필요했다.
            int_label = int_label.zfill(7) # 1.png와 001.png는 다른것이기 때문에 자릿수를 맞춰주었다.
            for f in files: #train 폴더 안에 있는 파일과 내가 만든 라벨링 되어 있는 파일명이 같은 것을 적절한 폴더가 이동시키는 반복문
                if int_label == f:
                    file_to_move = os.path.join(root, f)
                    shutil.move(file_to_move, "/home/jongkook/jongkookE/data/hand_classes_1/"+ str(dest))
for idx in range(11):
    a = globals()["var_{}".format(idx)]
    hand_classes(a,idx)


