# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 00:08:25 2023

@author: dell
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.metrics import accuracy_score
warnings.filterwarnings("ignore")
from mlxtend.frequent_patterns import apriori,association_rules

#loading our dataset
df = pd.read_csv("D:\\data science python\\NEW DS ASSESSMENTS\\Assosciation rules\\book.csv")
df

# Data Exploration
df.iloc[:,:].sum()

df.info()

for i in df.columns:
    print(i)
    print(df[i].value_counts())
    print()
    
#Data Visualization

from wordcloud import WordCloud

plt.rcParams['figure.figsize'] = (10, 8)
wordcloud = WordCloud(background_color = 'white', width = 1200,  height = 1200, max_words = 121).generate(str(df.sum()))
plt.imshow(wordcloud)
plt.axis('off')
plt.title('Items',fontsize = 20)
plt.show()

#1. Association rules with 10% Support and 30% confidence
movies1 = apriori(df, min_support=0.1, use_colnames=True)
movies1

rules = association_rules(movies1, metric="confidence", min_threshold=0.3)
rules

rules.sort_values('lift',ascending=False)
lift=rules[rules.lift>1]
lift

matrix = lift.pivot('antecedents','consequents','lift')
plt.figure(figsize=(20,6),dpi=250)
sns.heatmap(matrix,annot=True)
plt.title('HeatMap - ForLiftMatrix')
plt.yticks(rotation=0)
plt.xticks(rotation=90)

# visualization of obtained rule
sns.scatterplot(x=rules['support'],y=rules['confidence'])

#2. Association rules with 15% Support and 50% confidence
movies2 = apriori(df, min_support=0.15, use_colnames=True)
movies2

rules = association_rules(movies2, metric="confidence", min_threshold=0.5)
rules

rules.sort_values('lift',ascending=False)
lift=rules[rules.lift>1]
lift

matrix = lift.pivot('antecedents','consequents','lift')
plt.figure(figsize=(20,6),dpi=250)
sns.heatmap(matrix,annot=True)
plt.title('HeatMap - ForLiftMatrix')
plt.yticks(rotation=0)
plt.xticks(rotation=90)

# visualization of obtained rule
sns.scatterplot(x=rules['support'],y=rules['confidence'])

#3. Association rules with 17% Support and 40% confidence
movies3 = apriori(df, min_support=0.17, use_colnames=True)
movies3

rules = association_rules(movies3, metric="confidence", min_threshold=0.4)
rules

rules.sort_values('lift',ascending=False)
lift=rules[rules.lift>1]
lift

matrix = lift.pivot('antecedents','consequents','lift')
plt.figure(figsize=(20,6),dpi=250)
sns.heatmap(matrix,annot=True)
plt.title('HeatMap - ForLiftMatrix')
plt.yticks(rotation=0)
plt.xticks(rotation=90)

# visualization of obtained rule
sns.scatterplot(x=rules['support'],y=rules['confidence'])
