import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.models import Sequential

(x_train, y_train),(x_test,y_test) = tf.keras.datasets.mnist.load_data() #mnist 데이터 불러오기

x_train = x_train.reshape(x_train.shape[0], 28, 28, 1).astype("float32")/255 #keras는 값이 0~1사이에 있을때 최적의 성능을 보이기때문에 0~1사이의 값으로 변환
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1).astype("float32")/255 #데이터 
x_train, x_test = x_train / 255.0, x_test / 255.0 

y_train = tf.keras.utils.to_categorical(y_train, 10)  #데이터를 원핫인코딩으로 전환해주는 코드
y_test = tf.keras.utils.to_categorical(y_test, 10)

model = Sequential() # 단 하나의 입력층과 단 하나의 출력층이 있을 때 사용하는 모델
model.add(Conv2D(32, kernel_size=(3,3), input_shape=(28,28,1), activation="relu")) #keras에서 컨볼루션 층을 추가하는 함수 (커널을 몇개 적용할지, 커널의 크기, 맨 처음에 입력되는 값, 활성화 함수)
model.add(Conv2D(64, (3,3), activation="relu")) # 컨볼루션 층을 하나 더 추가, 3*3 크기의 커널을 64개 적용 활성화 함수 = relu
model.add(MaxPooling2D(pool_size=2)) #컨볼루션층에서 이미지 특징을 도출했지만 그 결과가 너무 크고 복잡해서 풀링을 사용, 정해진 구역에서 최댓값을 뽑아내는 MaxPooling 사용
model.add(Dropout(0.25)) #괴적합을 효과적으로 피해주기 위해서 드랍아웃을 사용 랜덤하게 25퍼센트의 노드들을 끔으로써 과적합을 방지, 과적합이란 학습 데이터에 대해 과하게 학습하여 실제 데이터에 대한 오차가 증가하는 현상
model.add(Flatten()) # 이제 기본 층에 연결하기 위해서 2차원 배열을 1차원 배열로 바꿔줌.
model.add(Dense(128,activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(10,activation="softmax"))

model.compile(loss="categorical_crossentropy", optimizer = "Adam", metrics=["accuracy"])
model.summary()

history=model.fit(x_train, y_train, batch_size=100, epochs = 10, validation_data = (x_test, y_test))

y_test_loss = history.history["val_loss"]
y_loss = history.history["loss"]
x_len = np.arange(len(y_loss))
plt.plot(x_len, y_test_loss, marker=".", c ="red", label="Testset_loss")
plt.plot(x_len, y_loss, marker=".", c ="blue", label="Trainset_loss")

plt.legend(loc = "upper right")
plt.grid()
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()
