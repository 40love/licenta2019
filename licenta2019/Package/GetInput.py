'''
Created on Apr 24, 2019

@author: PITA
'''
from PIL import Image
import numpy
import os
from builtins import isinstance

directorImaginiInput="..\..\Radiografii_DB"
directorImaginiOutput="..\..\Radiografii_DB_Output"
dimensiune = (200,200)
dimensiuneOut = (50,50)
factorZoom = dimensiune[0]/dimensiuneOut[0]
def tranformaImagine(imagine):
    imagine=Image.open(imagine).convert('L')
    #image = color.rgb2gray(imagine)
    image_resized = imagine.resize(dimensiune,Image.ANTIALIAS)
    pixels = list(image_resized.getdata())
    width, height = image_resized.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    return pixels

def getPixeliOutput(fisier):
    output = []
    # import the necessary packages
    import imutils
    import cv2
    

    # load the image, convert it to grayscale, blur it slightly,
    # and threshold it
    image = cv2.imread(fisier)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red = numpy.array([0,100,100])
    upper_red = numpy.array([179, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    #cv2.imshow("HSV", hsv)
   # cv2.waitKey(0)
   # cv2.imshow("Mask", mask)
   # cv2.waitKey(0)
    
    blurred = cv2.GaussianBlur(mask, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
    # find contours in the thresholded image
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # Create a black image
    img = numpy.zeros((600,600,3), numpy.uint8)
    for c in cnts:
        # compute the center of the contour
        M = cv2.moments(c)
        print(M["m10"])
        print(M["m00"])
        print(M["m01"])
        if M["m00"] != 0.0 :
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])   
            output.append([cX,cY])
            cv2.circle(img,(cX,cY), 3, (0,0,255), -1)
    
    print(fisier)  
    print(output)
    #cv2.imshow("Mask", img)
    #cv2.waitKey(0)
    return output

def prelucreazaImagineOutput(fisier):
    numeComplet = os.path.join(directorImaginiOutput,fisier)
    pixeliOutput = getPixeliOutput(numeComplet)
    cheieDictionar = fisier.split(".")[0]
    if cheieDictionar not in dictionarImagini:
        dictionarImagini[cheieDictionar]=[0,0]
    y_t = []
    y = [-1]*dimensiuneOut[0]
    for _ in range(dimensiuneOut[1]):
        y_t.append(y)
    for pixel in pixeliOutput:
        y_t[int(pixel[0]/factorZoom)][int(pixel[1]/factorZoom)] = 1
    
    dictionarImagini[cheieDictionar][1]=y_t
    return y_t

def prelucreazaImagineInput(fisier):
    numeComplet = os.path.join(directorImaginiInput,fisier)
    img = tranformaImagine(numeComplet)
    img=numpy.reshape(img,(dimensiune[0],dimensiune[1],1))
    if fisier.split(".")[0] not in dictionarImagini:
        dictionarImagini[fisier.split(".")[0]] = [0,0]
    
    dictionarImagini[fisier.split(".")[0]][0]=img
    return img
    

dictionarImagini={}  #dictionar[NumeImagine] = [intrarePiexeli,iesirePixelCarii]

def resizePoza(directorImagini,fisier):
    numeComplet = os.path.join(directorImagini,fisier)
    imagine=Image.open(numeComplet)#.convert('L')
    image_resized = imagine.resize(dimensiune,Image.ANTIALIAS)
    numeOutput = fisier.split(".")[0] + "aux"+"."+fisier.split(".")[1]
    numeComplet = os.path.join(directorImagini,numeOutput)
    image_resized.save(numeComplet)
    return numeOutput

def mainInput():
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(directorImaginiInput) if isfile(join(directorImaginiInput, f))]
    for fisier in onlyfiles:
        if (fisier.endswith("jpg") or fisier.endswith("png") ) and "aux" not in fisier:
            fisier = resizePoza(directorImaginiInput,fisier)
            prelucreazaImagineInput(fisier)
            
    onlyfiles = [f for f in listdir(directorImaginiOutput) if isfile(join(directorImaginiOutput, f))]
    for fisier in onlyfiles:
        if (fisier.endswith("jpg") or fisier.endswith("png") ) and "aux" not in fisier:
            fisier = resizePoza(directorImaginiOutput,fisier)
            prelucreazaImagineOutput(fisier)
            
    intrare = []
    iesire = []
    for valori in dictionarImagini.values():
        if(not isinstance(valori[0],int)) and (not isinstance(valori[1], int)):
            intrare.append(valori[0])
            iesire.append(valori[1])
    intrare = numpy.array(intrare)
    iesire =numpy.array(iesire)
    print(len(intrare), len(iesire))
    return intrare,iesire

#mainInput()