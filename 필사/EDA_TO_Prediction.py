import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("fivethirtyeight")

path = "/home/jongkook/jongkookE/data/titanic/"
train = pd.read_csv(path+"train.csv")
test = pd.read_csv(path+"test.csv")

print(train.head())

print(train.isnull().sum())

# how many survived??

f, ax = plt.subplots(1,2, figsize = (8,6))
train["Survived"].value_counts().plot.pie(explode = [0,0.05], autopct = "%1.1f%%", ax = ax[0], shadow = True)
ax[0].set_title("Survived")
ax[0].set_ylabel("")
sns.countplot("Survived", data = train, ax=ax[1])
ax[1].set_title("Survived")
#plt.show()

print(train.groupby(["Sex", "Survived"])["Survived"].count())

f, ax = plt.subplots(1,2, figsize=(8,8))
train[["Sex", "Survived"]].groupby(["Sex"]).mean().plot.bar(ax=ax[1])
ax[1].set_title("Survived vs Sex")
sns.countplot("Sex", hue="Survived", data = train, ax=ax[0])
ax[0].set_title("Sex:Survived vs Dead")
#plt.show()

crs_tb = pd.crosstab(train.Pclass, train.Survived, margins=True)
print(crs_tb)

f, ax = plt.subplots(1,2,figsize = (8,8))
train["Pclass"].value_counts().plot.bar(ax=ax[0])
ax[0].set_title("Number of Passange By Pclass")
ax[0].set_ylabel("Count")
sns.countplot("Pclass", hue="Survived", data = train, ax=ax[1])
ax[1].set_title("Pclass: Survived vs Dead")
#plt.show()

print(pd.crosstab([train.Sex, train.Survived], train.Pclass, margins = True))

sns.factorplot("Pclass", "Survived", hue="Sex", data = train)
#plt.show()

print(f"제일 연장자의 나이: {train['Age'].max()}살")
print(f"제일 나이가 적은 사람의 나이: {train['Age'].min()}살")
print(f"평균 나이: {train['Age'].mean()}살")

f, ax = plt.subplots(1,2,figsize = (8,8))
sns.violinplot("Pclass", "Age", hue="Survived", data = train, ax=ax[0], split = True)
ax[0].set_title("Pclass and Age VS Survived")
ax[0].set_yticks(range(0,110,10))
sns.violinplot("Sex", "Age", hue="Survived", data = train, ax=ax[1], split = True)
ax[1].set_title("Sex and Age VS Survived")
ax[1].set_yticks(range(0,110,10))
#plt.show()

print("정규식을 이용해 Initial을 뽑아낸다는데 난 이게 참 뭔소린지... 모르겠다...?")
train["Initial"] = 0
for i in train:
    train["Initial"] = train.Name.str.extract("([A-Za-z]+)\.")

print(pd.crosstab(train.Initial,train.Sex))

train["Initial"].replace(['Mlle','Mme','Ms','Dr','Major','Lady','Countess','Jonkheer','Col','Rev','Capt','Sir','Don'],
['Miss','Miss','Miss','Mr','Mr','Mrs','Mrs','Other','Other','Other','Mr','Mr','Mr'],inplace = True)

print(train.groupby("Initial")["Age"].mean())

train.loc[(train.Age.isnull())&(train.Initial=='Mr'),'Age']=33
train.loc[(train.Age.isnull())&(train.Initial=='Mrs'),'Age']=36
train.loc[(train.Age.isnull())&(train.Initial=='Master'),'Age']=5
train.loc[(train.Age.isnull())&(train.Initial=='Miss'),'Age']=22
train.loc[(train.Age.isnull())&(train.Initial=='Other'),'Age']=46

f, ax = plt.subplots(1,2, figsize = (10,10))
train[train["Survived"]==0].Age.plot.hist(ax=ax[0], bins=20, edgecolor = "black", color="red")
ax[0].set_title("Survived==0")
x1=list(range(0,85,5))
ax[0].set_xticks(x1)
train[train["Survived"]==1].Age.plot.hist(ax=ax[1], bins=20, edgecolor = "black", color="magenta")
ax[1].set_title("Survived==1")
ax[1].set_xticks(x1)


sns.factorplot("Pclass", "Survived", col="Initial", data = train)
plt.show()