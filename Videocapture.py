import cv2,time
video=cv2.VideoCapture(0)
a=1
while True:
    a=a+1
    check,frame=video.read()
    print(check,frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    print(gray)
    cv2.imshow("Capture",gray)
    key=cv2.waitKey(1)
    if a==300:
        break
     
print(a)
video.release()
cv2.destroyAllWindows()   
