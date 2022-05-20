import pandas as pd
import os
import shutil

train_csv = pd.read_csv("/home/jongkook/문서/jk_Ai/code/handpose/train.csv")
train_csv['label'][train_csv['label'] == '10-1'] = 10 ## label : 10-1 -> 10
train_csv['label'][train_csv['label'] == '10-2'] = 0 ## Label : 10-2 -> 0
train_csv['label'][train_csv['label'] == '1'] = 1
train_csv['label'][train_csv['label'] == '2'] = 2 
train_csv['label'][train_csv['label'] == '3'] = 3
train_csv['label'][train_csv['label'] == '4'] = 4
train_csv['label'][train_csv['label'] == '5'] = 5
train_csv['label'][train_csv['label'] == '6'] = 6
train_csv['label'][train_csv['label'] == '7'] = 7
train_csv['label'][train_csv['label'] == '8'] = 8
train_csv['label'][train_csv['label'] == '9'] = 9

# 10-1과 10-2는 라벨명을 수정하기 위한것이 였지만 나머지 숫자들은 tolist를 제대로 하기 위해서 
# 라벨 값을 str형태에서 int형태로 수정하기 위해서 바꾼것이다.
# 저런 야매식말고 제대로 된 타이핑 방법을 배워두면 더 편하게 쓸 수 있을 것 같다.

train_csv.index = train_csv.index + 1 # index는 0부터 시작하기 때문에 +1 해주어서 index값이 1부터 시작하게 변경

label_index_0=train_csv.index[train_csv["label"]==0].tolist() 
label_index_1=train_csv.index[train_csv["label"]==1].tolist()
label_index_2=train_csv.index[train_csv["label"]==2].tolist()
label_index_3=train_csv.index[train_csv["label"]==3].tolist()
label_index_4=train_csv.index[train_csv["label"]==4].tolist()
label_index_5=train_csv.index[train_csv["label"]==5].tolist()
label_index_6=train_csv.index[train_csv["label"]==6].tolist()
label_index_7=train_csv.index[train_csv["label"]==7].tolist()
label_index_8=train_csv.index[train_csv["label"]==8].tolist()
label_index_9=train_csv.index[train_csv["label"]==9].tolist()
label_index_10=train_csv.index[train_csv["label"]==10].tolist()

# label값이 0인 것부터 10인것까지 전부다 리스트형태로 바꿔줌
# 이것도 반복문을 사용하면 간결하게 쓸 수 있을것같지만 일단 야매로 노가다하여 수정

def hand_classes(label_index, dest): 
    for root, files in os.walk("/home/jongkook/문서/jk_Ai/code/handpose/train"): # root, files subdir은 변수가 아닌 실제 경로 안의 루트, 파일 서브 디렉토리를 의미
        for i in range(len(label_index)):
            int_label = str(label_index[i]) + ".png" # 나는 인덱스의 숫자를 파일명의 label과 맞추었기 때문에 추가적으로 인덱스 값 뒤에 ".png"를 넣는 추가 작업이 필요했다.
            int_label = int_label.zfill(7) # 1.png와 001.png는 다른것이기 때문에 자릿수를 맞춰주었다.
            for f in files: #train 폴더 안에 있는 파일과 내가 만든 라벨링 되어 있는 파일명이 같은 것을 적절한 폴더가 이동시키는 반복문
                if int_label == f:
                    file_to_move = os.path.join(root, f)
                    shutil.move(file_to_move, "/home/jongkook/문서/jk_Ai/code/hand_classes/"+ str(dest))

hand_classes(label_index_0, 0) # 이것도 반복문을 쓰고 싶었지만 실력부족으로 야매식으로 풀었음
hand_classes(label_index_1, 1)
hand_classes(label_index_2, 2)
hand_classes(label_index_3, 3)
hand_classes(label_index_4, 4)
hand_classes(label_index_5, 5)
hand_classes(label_index_6, 6)
hand_classes(label_index_7, 7)
hand_classes(label_index_8, 8)
hand_classes(label_index_9, 9)
hand_classes(label_index_10, 10)

