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
