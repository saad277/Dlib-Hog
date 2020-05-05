import cv2
import dlib
from imutils import face_utils

detector=dlib.get_frontal_face_detector();



image=cv2.imread("./image2.JPG")

cv2.imshow("image",image)
cv2.waitKey(0);
cv2.destroyAllWindows();


gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

face=detector(gray,1)

for i in face:
    x1 = i.left()
    y1 = i.top()
    x2 = i.right()
    y2 = i.bottom() 
    cv2.rectangle(image,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow("detected",image)
cv2.waitKey(0);
cv2.destroyAllWindows();



    
