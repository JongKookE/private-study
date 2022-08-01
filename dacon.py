import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import Image
import seaborn as sns

path = "/content/drive/MyDrive/Colab Notebooks/데이터/심리예측/"

train = pd.read_csv(path+"train.csv")
test = pd.read_csv(path+"test.csv")
sample = pd.read_csv(path+"sample_submission.csv")

Q_eda = ["Q1","Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10", "Q11", "Q12", "Q13", "Q14", "Q15", "Q16", "Q17", "Q18", "Q19", "Q20", "Q21", "Q22", "Q23", "Q24", "Q25", "Q26"]
tipi = ["TIPT1", "TIPI2", "TIPI3", "TIPI4", "TIPI5", "TIPI6", "TIPI7", "TIPI8", "TIPI9", "TIPI10",
        "VCL1", "VCL2", "VCL3", "VCL4", "VCL5", "VCL6", "VCL7", "VCL8", "VCL9", "VCL10", "VCL11", "VCL12"       
        , "VCL13", "VCL14", "VCL15", "VCL16"]

correlations = train[Q_eda].corr(method = 'spearman')
sns.heatmap(correlations, cmap="coolwarm", square=True, center=0)
