'''
Created on Apr 24, 2019

@author: PITA
'''
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D, Input,Flatten,Reshape
from keras import optimizers
from keras import  regularizers
dimensiune = (200,200)
def getModel():
    global model2
    return model2
digit_input = Input(shape=(dimensiune[0], dimensiune[1],1), name='main_input')
x=Conv2D(40,(5,5),activation='relu',kernel_regularizer=regularizers.l2(0.01), name='main_input2')(digit_input)
x=MaxPooling2D((2,2))(x)
x=Conv2D(40,(5,5),activation='relu',kernel_regularizer=regularizers.l2(0.01), name='main_input3')(x)
#x=MaxPooling2D((2,2))(x)
x=Flatten()(x)
x=Dense(100,activation='relu',kernel_regularizer=regularizers.l2(0.01))(x)
x=Dense(100,activation='relu',kernel_regularizer=regularizers.l2(0.01))(x)
out=Dense(dimensiune[0]*dimensiune[1],activation='relu',kernel_regularizer=regularizers.l2(0.01))(x)
out = Reshape(dimensiune)(out)
model2 = Model(digit_input, out)
print(model2)
sgd = optimizers.sgd(lr=30) 
model2.compile(optimizer=sgd,
              loss='categorical_crossentropy',
              metrics=['accuracy'])