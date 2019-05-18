'''
Created on Apr 24, 2019

@author: PITA
'''
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D, Input,Flatten,Reshape,Dropout
from keras import optimizers
from keras import  regularizers
from keras.regularizers import l2
import keras.metrics
import keras.backend as K
import tensorflow as tf

dimensiune = (200,200)

def carenteTotale(y_true, y_pred):
    
    return K.sum(K.cast(K.equal(y_true,K.sign(y_pred)),tf.int16))
    
    
def pusaCarieSiNuE(y_true, y_pred):
    aux1 = K.not_equal(y_true,K.sign(y_pred))
    return K.sum(K.cast(K.equal(aux1,K.cast(K.sign(y_pred),tf.bool)),tf.int16))
    

def trebeCarieSiNaPus(y_true, y_pred):
    aux1 = K.not_equal(y_true,K.sign(y_pred))
    aux2 =  K.not_equal(K.ones(K.shape(y_pred)),K.sign(y_pred))
    return K.sum(K.cast(K.equal(aux1,aux2),tf.int16))
def getModel():
    global model
    return model

model = Sequential()
# input: 100x100 images with 3 channels -> (100, 100, 3) tensors.
# this applies 32 convolution filters of size 3x3 each.
model.add(Conv2D(32, (3, 3), activation='elu',W_regularizer=l2(1e-6), input_shape=(dimensiune[0], dimensiune[1], 1)))
model.add(Conv2D(32, (3, 3), activation='elu',W_regularizer=l2(1e-6)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation='elu',W_regularizer=l2(1e-6)))
model.add(Conv2D(64, (3, 3), activation='elu',W_regularizer=l2(1e-6)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256, activation='elu',W_regularizer=l2(1e-6)))
model.add(Dropout(0.5))
model.add(Dense(2500, activation='elu',W_regularizer=l2(1e-6)))
model.add(Reshape((50,50)))

adag = optimizers.Adagrad(lr=0.01, epsilon=1e-9)
sgd = optimizers.SGD(lr=0.1, decay=1e-6, momentum=0.5, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=[carenteTotale,pusaCarieSiNuE,trebeCarieSiNaPus])
