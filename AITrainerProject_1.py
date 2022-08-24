import cv2
import PoseModule as pm
import time
import numpy as np


cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
dir = 0
pTime=0
second = 0
minute = 0
while True:
    success, img = cap.read()
    img = cv2.resize(img,(1280,720))
    img = detector.findPose(img,False)
    lmList = detector.findPosition(img,False)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    #print(lmList)
    if len(lmList) !=0:
        ## Right Arm
        #detector.findAngle(img,12,14,16) 
        # Left Arm
        angle_l= detector.findAngle(img,11,13,15) 
        angle_r= detector.findAngle(img,12,14,16) 
        # per_l = np.interp(angle_l,(0,180),(0,100))
        # # bar_l = np.interp(angle_l,(0,180),(650,100))
        # per_r = np.interp(angle_r,(0,180),(0,100))
        # # bar_r = np.interp(angle_r,(180,360),(650,100))
        # #print(angle,per)  
        
        if ((angle_l>50 and angle_l<150) and (angle_r>50 and angle_r<150)) or  ((angle_l>220 and angle_l<330) and (angle_r>220 and angle_r<330)) or ((angle_l>220 and angle_l<330) and (angle_r>50 and angle_r<150)) or  ((angle_l>50 and angle_l<150) and (angle_r>220 and angle_r<330)):
            time.sleep(1)    
            second+=1    
            if(second == 60):    
                second = 0    
                minute+=1

            counter = second+60*minute
            cv2.putText(img,str('Plank timing:'),(700,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
            cv2.putText(img,str(int(counter)),(1000,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
            
        else:
            cv2.putText(img,str("Let's do good plank"),(700,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)       

    cv2.putText(img,str(int(fps)),(50,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow('Image',img)
    cv2.waitKey(1)