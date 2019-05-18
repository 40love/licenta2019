'''
Created on Apr 24, 2019

@author: PITA
'''
from Package import GetInput, Retea
import numpy
limita = 0.5
def tipareste(x):
    lst=[]
    for it in range(len(x)):
        for jt in range(len(x[it])):
          if x[it][jt] not in lst:
              lst.append(x[it][jt])
    lst.sort()
    print(lst)  
def analizeazaPoza(poza):
    import cv2
    pixeli = GetInput.prelucreazaImagineInput(poza)
    image = cv2.imread(poza)
    model = Retea.getModel()
    pred = model.predict(numpy.array([pixeli]))
    suma = 0
    cnt = 0
    for it in range(len(pred[0])):
        
        for jt in range(len(pred[0][it])):
            
            if pred[0][it][jt]>limita:
                suma +=pred[0][it][jt]
                cnt +=1
    medie = (float(suma)/float(cnt))
    for it in range(len(pred[0])):
        for jt in range(len(pred[0][it])):
            if pred[0][it][jt]>medie:    
                cv2.circle(image,(it*4,jt*4), 3, (0,0,255), -1)
    tipareste(pred)
    cv2.imshow("IataCarii", image)
    cv2.waitKey(0)
    print(medie)
    print(pred.shape)
    print(pred)
    
    
#analizeazaPoza(r"C:\Users\PITA\git\licenta2019\Radiografii_DB\PHOTO-2019-04-24-14-12-50.jpg")