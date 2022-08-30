import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno # null 값을 처리하는데 적합한 모듈
plt.style.use('seaborn')
sns.set(font_scale=2.5)
import warnings
warnings.filterwarnings('ignore')

train = pd.read_csv("/home/jongkook/jongkookE/data/titanic/train.csv")
test = pd.read_csv("/home/jongkook/jongkookE/data/titanic/test.csv")
#print(train.head())

titanic_info = pd.DataFrame({"변수":["survival", "Pclass", "sex", "Age", "sibSp", "parch", "ticket", "fare"
, "cabin", "embarked"],
"정의": ["생존여부", "티켓의 클래스", "성별", "나이", "함께 탑승한 형제와 배우자의 수", "함께 탑승한 부모, 아이의 수",
"티켓 번호", "탑승료", "객실 번호", "탑승 항구"],
"타입":["integer", "integer", "string", "integer", "integer", "integer", "string", "float", "string", "string"]
}) #타이타닉 데이터의 정보

#print(titanic_info.shape)

print(train.describe, test.describe)

print(f"train's shape[0] = {train.shape[0]}") 
def null_data(data):
    for col in data.columns: #Null Data 체크
        msg = "column: {:>10}\t Percent of NaN Value: {:2f}%".format(col, 100*(data[col]. isnull().sum()/data[col].shape[0]))
        print(msg)
null_data(train)
print("-"*100)
null_data(test)


#msno.matrix(df=train.iloc[:,:], figsize = (8,8), color = (0.8, 0.5, 0.2)) # 정상적이라면 그래프가 나와서 시각적 효과가 있지만 나는 안되네

# target Label 확인

f, ax = plt.subplots(1,2, figsize=(18,8))


"""train['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True) #이것도 그래프가 안나오네
ax[0].set_title("Pie plot - Sruvived")
ax[0].set_ylabel("")
sns.countplot("Survived", data = train, ax = ax[1])
ax[1].set_title("count plot = Survived")

plt.show()"""

print(train.shape)

print(train[["Pclass", "Survived"]].groupby(["Pclass"], as_index = True).sum())

print(pd.crosstab(train["Pclass"], train["Survived"], margins = True))

#sur = train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=True).mean().sort_values(by='Survived', ascending=False).plot.bar()

print(sns.factorplot("Pclass", "Survived", hue = "Sex", data=train, size = 6, aspect = 1.5))

print(train.columns)