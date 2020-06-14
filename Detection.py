import cv2
import numpy
from matplotlib import pylab

def roi (image,vertices):
    mask=numpy.zeros_like(image)
    #channel=img.shape[2]
    match_color=255
    cv2.fillPoly(mask,vertices,match_color)
    masked_image=cv2.bitwise_and(image,mask)
    return masked_image

def draw_lines (img,lines):
    img=img.copy()
    blank_image=numpy.zeros_like(img,dtype=numpy.uint8)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(blank_image,(x1,y1),(x2,y2),(0,255,0),2)

    img=cv2.addWeighted(img,0.8,blank_image,1,0)
    return img

img=cv2.imread('Test.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

print(img.shape)
height= img.shape[0]
width=img.shape[1]

roi_vertices=[
    (width/2,height),
    (width/2,height/2),
    (width/1.65,height/2),
    (width,height/1.25),
    (width,height)
]

grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(grayimg,75,150)
crop=roi(canny,numpy.array([roi_vertices],numpy.int32))
lines=cv2.HoughLinesP(crop,rho=6,theta=numpy.pi/60,threshold=160,lines=numpy.array([]),minLineLength=40,maxLineGap=25)
line_image=draw_lines(img,lines)

pylab.imshow(line_image)
pylab.show()