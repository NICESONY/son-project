import pandas as pd

date = pd.read_csv('C:/Users/손건희/Desktop/gpascore.csv')
print(date)

# print(date.isnull().sum())
date = date.dropna()
# print(date.isnull().sum())
# date = data.fillna(100)
# date(date['gpa'].count())

y데이터 = date['admit'].values
# print(y데이터)


x데이터 = [  ]



for i, rows in  date.iterrows():
    x데이터.append([ rows['gre'], rows['gpa'],rows['rank'] ]) 

print(x데이터)

exit()

import numpy as np
import tensorflow as tf


model = tf.keras.models.Sequential([
    tf.keras.layers.dense(64,activation = 'tanh'),
    tf.keras.layers.dense(128,activation = 'tanh'),
    tf.keras.layers.dense(1,activation = 'sigmoid'),
])


model.compile(optimizer= 'adam' , loss= 'binary_crossentropy' ,  metrics=['accuracy'])


model.fit( np.array(x데이터), np.array(y데이터), epochs=1000)

# 예측값 = model.predict( [ [750,3.70,3], [400,2.2,1] ])
# print(예측값)