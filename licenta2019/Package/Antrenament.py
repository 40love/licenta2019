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
from Package.MainScript import analizeazaPoza
from keras.models import model_from_json

def mainAntrenament() :
    #session = tf.Session(config=tf.ConfigProto(log_device_placement=True))
    intrare, iesire  = mainInput()
    #intrare = numpy.tile(intrare,10)
    #iesire = numpy.tile(iesire, 10)
    model = Retea.getModel()
    
    model.fit (intrare,iesire,epochs=10,batch_size=10,shuffle=True,validation_split=0.1)
    salveazaModel(model)

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
    
   
   
def salveazaModel(model):     
        # serialize model to JSON
        model_json = model.to_json()
        with open("model.json", "w") as json_file:
            json_file.write(model_json)
        # serialize weights to HDF5
        model.save_weights("model.h5")
        print("Saved model to disk")
 
def incarcaModel():
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")
    return loaded_model
    

mainAntrenament()
deleteAuxFiles("..\..\Radiografii_DB") 
deleteAuxFiles("..\..\Radiografii_DB_Output") 
analizeazaPoza(r"C:\Narcis\repos\licenta2019\Radiografii_DB\PHOTO-2019-04-20-15-56-23.jpg")
