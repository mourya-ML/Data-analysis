# -*- coding: utf-8 -*-
"""20MBMB04 (1) (1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eKuE1ULoIqbbg6XyVEbTMV3NIYVNwMv3
"""

import pandas as pd

dataset = pd.read_csv('/content/drive/MyDrive/emerging_trends/Churn_Modelling (1).csv')
dataset = dataset.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

one_hot_geo = pd.get_dummies(dataset['Geography'])

dataset = dataset.drop('Geography',axis = 1)

dataset= dataset.join(one_hot_geo)

one_hot_gen = pd.get_dummies(dataset['Gender'])
dataset = dataset.drop('Gender',axis = 1)
dataset= dataset.join(one_hot_gen)

X = dataset.iloc[:, [0,1,2,3,4,5,6,7,9,10,11,12,13]].values
y = dataset.iloc[:, 8].values
y

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
n_features = X_train.shape[1]

model = Sequential()
model.add(Dense(6, activation='relu', kernel_initializer='he_normal', input_shape=(n_features,)))
model.add(Dense(8, activation='relu', kernel_initializer='he_normal'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=0)

loss, acc = model.evaluate(X_test, y_test, verbose=0)
print('Test Accuracy: %.3f' % acc)

score =model.evaluate(X_test, y_test, batch_size=10)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

from sklearn.metrics import classification_report
target_names = ['class 0', 'class 1']
print(classification_report(y_test, y_pred, target_names=target_names))

dataset

import numpy as np
from imblearn.over_sampling import ADASYN

dataset['Exited'].values

X=dataset.iloc[:,0:13]
Y=dataset['Exited']

resampler= ADASYN()
X_resampled, Y_resampled = resampler.fit_resample(X,Y)

oversampled = pd.concat([pd.DataFrame(X_resampled), pd.DataFrame(Y_resampled)], axis=1)
oversampled.columns = dataset.columns

print("X.shape: {}, Y.shape: {}".format(X_resampled.shape, Y_resampled.shape))
print("{} '0' labels, {} '1' labels".format(sum(Y_resampled==0), sum(Y_resampled==1)))

X = oversampled.iloc[:, [0,1,2,3,4,5,6,7,9,10,11,12,13]].values
Y = oversampled.iloc[:, 8].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 4)

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
n_features = X_train.shape[1]
model = Sequential()
model.add(Dense(64, activation='relu', kernel_initializer='he_normal', input_shape=(n_features,)))
model.add(Dense(16, activation='relu', kernel_initializer='he_normal'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, Y_train, epochs=100, batch_size=32, verbose=0)

loss, acc = model.evaluate(X_test, Y_test, verbose=0)
print('Test Accuracy: %.3f' % acc)

score =model.evaluate(X_test, Y_test, batch_size=10)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

Y_pred = model.predict(X_test)
Y_pred = (Y_pred > 0.5)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)

from sklearn.metrics import classification_report
target_names = ['class 0', 'class 1']
print(classification_report(Y_test, Y_pred, target_names=target_names))