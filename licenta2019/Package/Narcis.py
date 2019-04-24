'''
Created on Apr 21, 2019

@author: PITA

'''
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D, Input,Flatten,Reshape
from keras import optimizers
from keras import  regularizers
import numpy
from PIL import Image
dimensiune = (200,200)
def tranformaImagine(imagine):
    imagine=Image.open(imagine).convert('L')
    #image = color.rgb2gray(imagine)
    image_resized = imagine.resize(dimensiune,Image.ANTIALIAS)
    image_resized.save("dinti4.png")
    pixels = list(image_resized.getdata())
    width, height = image_resized.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    return pixels
def test(net):
    for it in range(0,10):
        img=tranformaImagine(r"C:\Users\Pita\Desktop\cifre\cifra"+str(it)+r".png")
        x=[]
        img=numpy.reshape(img,(28,28,1))
        x.append(img)
        img=numpy.array(x)
        for kt in range(len(img)):
            img[kt]=1.0-img[kt]
        maxim=-10
        jt=0
        cifra=None
        for kt in net.predict(img):
            if kt[0]> maxim:
                maxim=kt[0]
                cifra=jt
            jt+=1
        print(it,cifra)
def inputImagine(imagine):
    img = tranformaImagine(imagine)
    img=numpy.reshape(img,(dimensiune[0],dimensiune[1],1))
    x = []
    y_t = [0]*dimensiune[0]
    y_j = []
    for it in range(dimensiune[1]):
        y_j.append(y_t)
    y_j[73][37]=1
    y = []
    for it in range(1000):
        x.append(img)
        y.append(y_j)
    img=numpy.array(x)
    y = numpy.array(y)
    return img,y

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

intrare,iesire = inputImagine(r"C:\Users\narci\Desktop\Radiografii\PHOTO-2019-04-20-15-56-23.jpg")
#model2.predict(intrare)
model2.fit(intrare, iesire, batch_size=15, epochs=10)
score = model2.evaluate(intrare, iesire, batch_size=15)