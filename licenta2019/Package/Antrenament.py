'''
Created on May 2, 2019

@author: narci
'''
import imutils
import numpy
print(imutils.__version__)
from Package.GetInput import mainInput
from Package import Retea
from Crypto.Random.random import shuffle
import tensorflow as tf

def mainAntrenament() :
    #session = tf.Session(config=tf.ConfigProto(log_device_placement=True))
    intrare, iesire  = mainInput()
    #intrare = numpy.tile(intrare,10)
    #iesire = numpy.tile(iesire, 10)
    model = Retea.getModel()
    
    model.fit (intrare,iesire,epochs=20,batch_size=128,shuffle=True,validation_split=0.1)
    
    
mainAntrenament()