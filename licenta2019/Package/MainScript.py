'''
Created on Apr 24, 2019

@author: PITA
'''
from Package import GetInput, Retea
import numpy
def analizeazaPoza(poza):
    pixeli = GetInput.prelucreazaImagineInput(poza)
    model = Retea.getModel()
    pred = model.predict(numpy.array([pixeli]))
    print(pred.shape)
    print(pred)
    
    
analizeazaPoza(r"C:\Users\PITA\git\licenta2019\Radiografii_DB\PHOTO-2019-04-24-14-12-50.jpg")