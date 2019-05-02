'''
Created on Apr 24, 2019

@author: PITA
'''
from Package import GetInput, Retea
import numpy
limita = 0.90
def analizeazaPoza(poza):
    import cv2
    pixeli = GetInput.prelucreazaImagineInput(poza)
    image = cv2.imread("dinti4.png")
    model = Retea.getModel()
    pred = model.predict(numpy.array([pixeli]))
    for it in range(len(pred[0])):
        for jt in range(len(pred[0][it])):
            if pred[0][it][jt]>limita:
                cv2.circle(image,(it,jt), 3, (0,0,255), -1)
    cv2.imshow("IataCarii", image)
    cv2.waitKey(0)
    print(pred.shape)
    print(pred)
    
    
analizeazaPoza(r"C:\Users\PITA\git\licenta2019\Radiografii_DB\PHOTO-2019-04-24-14-12-50.jpg")