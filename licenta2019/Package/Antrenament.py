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
    

#folder = r'C:\Users\PITA\git\licenta2019\Radiografii_DB'
def  deleteAuxFiles(folder):
    import os, shutil
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                if "aux" in file_path:
                    os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)
    print("Done")
    
deleteAuxFiles("..\..\Radiografii_DB") 
deleteAuxFiles("..\..\Radiografii_DB_Output") 

#mainAntrenament()