import cv2
import numpy as np
import pytesseract as pt

# m1=cv2.imread("3388.png",1)
# ret=pt.image_to_string(m1, "eng", "")
# print(ret)

# th, m2=cv2.threshold(m1, 240, 255, cv2.THRESH_BINARY)
# m2=cv2.erode(m2,
#     np.ones((1,15))
# )
# m2=cv2.cvtColor(m2,cv2.COLOR_BGR2GRAY)
# ct,th=cv2.findContours(m2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# for d in range(1,len(ct)):
#     x, y, w, h=cv2.boundingRect(ct[d])
#     if w>h*2:
#         m3=m1[y:y+h,x:x+w]
#
#         nh=100
#         nw=int((nh/m3.shape[0])*m3.shape[1])
#         m3=cv2.resize(m3,(nw,nh))
#
#         ret=pt.image_to_string(m3, "eng", "")
#         print(ret)
#
#         cv2.imshow("m3 "+str(d), m3)

from pyzbar import pyzbar
'''用攝像頭讀取QRcode'''
# m1=cv2.imread("wiki.png",1)
# c=cv2.VideoCapture(0)
# while c.isOpened()==True:
#     r,m1=c.read()
#     if r==True:
#         ret=pyzbar.decode(m1)
#         for d in ret:
#             print("類型:",d.type)
#             try:
#                 print("內容:",d.data.decode("utf-8").encode("sjis").decode("utf-8"))
#             except:
#                 print("內容:",d.data.decode("utf-8"))
#             x,y,w,h=d.rect
#             cv2.rectangle(m1,(x,y),(x+w,y+h),(0,0,255),2)
#
#             print("====================")
#         cv2.imshow("m1",m1)
#     if cv2.waitKey(33) & 0xFF == ord('q'):
#         break
#
# cv2.destroyAllWindows()

'''分類器辨識靜態圖片'''
# m1=cv2.imread("62334.jpg",1)
# c=cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")
#
# ret=c.detectMultiScale(m1,minNeighbors=1,minSize=(10,10))
# for x,y,w,h in ret:
#     cv2.rectangle(m1,(x,y),(x+w,y+h),(0,0,255),2)
#
# cv2.imshow("m1",m1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
'''以攝像頭捕捉辨識'''
a=cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")
c=cv2.VideoCapture(0)

while c.isOpened()==True:
    r,m1=c.read()
    if r==True:
        ret=a.detectMultiScale(m1,minNeighbors=3,minSize=(10,10))
        for x,y,w,h in ret:
            cv2.rectangle(m1,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow("m1",m1)
        if cv2.waitKey(33) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()