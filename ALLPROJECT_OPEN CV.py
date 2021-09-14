import cv2
import pafy
import pyautogui as p
import numpy as np



"""cap = cv2.VideoCapture(0)
while True:
    ret,frame =cap.read()
    frame =cv2.resize(frame,(700,500))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('rahul',gray)
    k=cv2.waitKey(25)
    if k == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()"""




#camera phone
"""""
camera = "https://192.168.11.7:8080/video"
cap = cv2.VideoCapture(0)
cap.open(camera)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("rahul.avi",fourcc,20.0,(640,480),0)

while cap.isOpened():
    ret,frame =cap.read()
    if ret == True:

        cv2.imshow("rahul",frame)
     #  output.wwrite("frame")
        if cv2.waitKey(1) == ord("Q"):
            break
cap.release()

cv2.destroyAllWindows()"""


# capture video from youtube

"""""
url = "https://www.youtube.com/watch?v=krJsyb_yf7A&list=RDMMkrJsyb_yf7A&start_radio=1"
data =pafy.new(url)
data = data.getbest(preftype="mp4")


cap = cv2.VideoCapture(0)
cap.open(data.url)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("rahul1.mp4",fourcc,20.0,(640,480),0)

while cap.isOpened():
    ret,frame =cap.read()
    if ret == True:

        cv2.imshow("rahul1",frame)
        output.write(frame)
        if cv2.waitKey(25) == ord("Q"):
            break
cap.release()
output.release()

cv2.destroyAllWindows()
"""



rs = p.size()

fps =60.0
fourcc =cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter("rah.mp4",fourcc,fps,rs)

cv2.namedWindow("live reco..",cv2.WINDOW_NORMAL)

while True:
    img = p.screenshot()
    f = np.array(img)
    f= cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
    output.write(f)
    cv2.imshow("live",f)
    if cv2.waitKey(25) == ord("Q"):
            break
output.release()
cv2.destroyAllWindows()

