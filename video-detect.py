import cv2
import dlib
from imutils import face_utils



face_detector=dlib.get_frontal_face_detector();


cap=cv2.VideoCapture(0);


while True:

    ret,frame=cap.read()


    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_detector(gray,1)


    for i in faces:
        x1 = i.left()
        y1 = i.top()
        x2 = i.right()
        y2 = i.bottom() 

        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.putText(frame,"Detected",(10,50),cv2.FONT_HERSHEY_SIMPLEX, 2, 255)

    cv2.imshow("detection",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    


cap.release();
cv2.destroyAllWindows();
