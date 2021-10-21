
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
import cv2
from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras import layers
import datetime
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import pandas as pd
#import tensorflow_datasets as tfds
import os


path = 'C:/Users/Dawid/Desktop/kurs/jdszr4-animalsi/gesty'

train = pd.read_csv(os.path.join(path,"dane/sign_mnist_train.csv"))

test = pd.read_csv(os.path.join(path,"dane/sign_mnist_test.csv"))

Y_train = train.iloc[:,0]
X_train = train.iloc[:,1:]
X_train = X_train.to_numpy()
Y_train = Y_train.to_numpy()

Y_test = test.iloc[:,0]
X_test = test.iloc[:,1:]
X_test = X_test.to_numpy()
Y_test= Y_test.to_numpy()


#zmiana ksztaltu naszego zbioru
X_train = X_train.reshape(-1,28,28)
X_test = X_test.reshape(-1,28,28)


#zmiana ksztaltu naszego zbioru Y
Y_train = Y_train.reshape(-1,1)
Y_train = OneHotEncoder(sparse = False).fit_transform(Y_train)

Y_test = Y_test.reshape(-1,1)
Y_test = OneHotEncoder(sparse = False).fit_transform(Y_test)


#normalizacja
X_train = X_train/255.0
X_test = X_test/255.0

#slownik zwracajacy nam przypisanie klasy do litery
slownik = {0: "A",
           1: "B",
           2: "C",
           3: "D",
           4: "E",
           5: "F",
           6: "G",
           7: "H",
           8: "I",
           9: "K",
           10: "L",
           11: "M",
           12: "N",
           13: "O",
           14: "P",
           15: "Q",
           16: "R",
           17: "S",
           18: "T",
           19: "U",
           20: "V",
           21: "W",
           22: "X",
           23: "Y"
          } 

