"""import cv2

img = cv2.imread('1.jpg')
#img =cv2.line(img,(30,30),(200,200),(0,0,255),5)
img=cv2.rectangle(img,(10,10),(50,50),(0,255,0),3)
img=cv2.circle(img,(10,10),5,(255,255,255),-1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"Hisham",(40,100),font,1,(255,0,0),2,-1)

img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""
import imutils
import cv2 
def detect(c):
    shape="undifined"
    length=cv2.arcLength(c, True)
    approx=cv2.approxPolyDP(c, 0.04*length, True)
    nop = len(approx)
    if nop==3:
        shape="triangle"
    elif nop==4:
        (x,y,w,h)=cv2.boundingRect(approx)
        s=float(w)/float(h)
        shape="square" if s>=0.95 and s<=1.05 else "rectangle"
    elif nop ==5 :
        shape="pentagon"
    else:
        shape="circle"
    return shape
        
            
img =cv2.imread('image.png')

gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

blur=cv2.GaussianBlur(gray, (5,5), 0)
thresh=cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)[1]
cnts =cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)

for c in cnts: 
    cv2.drawContours(img, [c], -1, (0,0,255),2)
    M =cv2.moments(c)
    cx=int((M["m10"]/M["m00"]))
    cy=int((M["m01"]/M["m00"]))
    shape=detect(c)
    cv2.putText(img, shape, (cx,cy), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
cv2.imshow('CONT',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
