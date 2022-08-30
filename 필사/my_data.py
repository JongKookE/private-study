import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
plt.style.use("fivethirtyeight")

path = "/home/jongkook/jongkookE/data/titanic/"
data = pd.read_csv(path+"train.csv")

def titanic(x):
    train = pd.read_csv(path+x+".csv")
    return train

def vis_Pclass_Fare(data):
    f,ax=plt.subplots(1,3,figsize=(20,8))
    sns.distplot(data[data['Pclass']==1].Fare,ax=ax[0])
    ax[0].set_title('Fares in Pclass 1')
    sns.distplot(data[data['Pclass']==2].Fare,ax=ax[1])
    ax[1].set_title('Fares in Pclass 2')
    sns.distplot(data[data['Pclass']==3].Fare,ax=ax[2])
    ax[2].set_title('Fares in Pclass 3')
    plt.show()

def corr_heatmap(for_test):
    sns.heatmap(for_test.corr(), annot = True, cmap="RdYlGn", linewidths = 0.2)
    fig=plt.gcf()
    fig.set_size_inches(20,15)
    plt.show()

def data_anal(data):
    data["Initial"] = 0
    for i in  data:
        data["Initial"] =   data.Name.str.extract("([A-Za-z]+)\.")

    data["Initial"].replace(['Mlle','Mme','Ms','Dr','Major','Lady','Countess','Jonkheer','Col','Rev','Capt','Sir','Don'],
    ['Miss','Miss','Miss','Mr','Mr','Mrs','Mrs','Other','Other','Other','Mr','Mr','Mr'],inplace = True)



    data.loc[(data.Age.isnull())&(data.Initial=='Mr'),'Age']=33
    data.loc[(data.Age.isnull())&(data.Initial=='Mrs'),'Age']=36
    data.loc[(data.Age.isnull())&(data.Initial=='Master'),'Age']=5
    data.loc[(data.Age.isnull())&(data.Initial=='Miss'),'Age']=22
    data.loc[(data.Age.isnull())&(data.Initial=='Other'),'Age']=46


    data["Age_band"] = 0
    data.loc[data['Age']<=16,'Age_band']=0
    data.loc[(data["Age"]>16) & (data["Age"]<=32), "Age_band"] = 1
    data.loc[(data["Age"]>32) & (data["Age"]<=48), "Age_band"] = 2
    data.loc[(data["Age"]>48) & (data["Age"]<=64), "Age_band"] = 3
    data.loc[data["Age"]>64, "Age_band"]=4
    #print(data.head())

    #print(data["Age_band"].value_counts().to_frame)

    #sns.factorplot("Age_band", "Survived", data= data, col="Pclass")
    #plt.show()

    data["FSZ"] = 0
    data["FSZ"] = data["SibSp"] + data["Parch"]
    data["Alone"] = 0
    data.loc[data.FSZ ==0, "Alone"]=1

    f, ax = plt.subplots(1,2, figsize =(18,6))
    sns.factorplot("FSZ", "Survived", data = data, ax=ax[0])
    ax[0].set_title("Family_Size VS Survived")
    sns.factorplot("Alone", "Survived", data = data, ax=ax[1])
    ax[1].set_title("Alone VS Survived")
    sns.factorplot('Alone','Survived',data=data,hue='Sex',col='Pclass')

    #plt.show()

    data["age_class"] = pd.cut(data["Age"], 3 , labels=["child", "adult", "older"])
    print(data[["Age" ,"age_class"]].head())

    sns.factorplot("Age", "age_class", data=data, hue = "Survived")
    plt.title("Age and age_class")

    data["fare_range"] = pd.qcut(data["Fare"],4)
    print(data.groupby(["fare_range"])["Survived"].mean().to_frame())

    data['Fare_cat']=0
    data.loc[data['Fare']<=7.91,'Fare_cat']=0
    data.loc[(data['Fare']>7.91)&(data['Fare']<=14.454),'Fare_cat']=1
    data.loc[(data['Fare']>14.454)&(data['Fare']<=31),'Fare_cat']=2
    data.loc[(data['Fare']>31)&(data['Fare']<=513),'Fare_cat']=3

    data['Sex'].replace(['male','female'],[0,1],inplace=True)
    data['Embarked'].replace(['S','C','Q'],[0,1,2],inplace=True)
    data['Initial'].replace(['Mr','Mrs','Miss','Master','Other'],[0,1,2,3,4],inplace=True)

    data.drop(["Name", "Age", "Ticket", "Fare", "Cabin", "fare_range", "PassengerId"], axis=1, inplace =True)
    sns.heatmap(data.corr(), annot = True,  linewidths = 0.2, annot_kws={"size":20})
    fig=plt.gcf()
    fig.set_size_inches(18,15)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.show()

    #plt.show()