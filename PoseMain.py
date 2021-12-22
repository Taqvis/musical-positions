import cv2 as cv
import time
import PoseModule as pm
import MusicModule as mm

capture = cv.VideoCapture(0)
pTime = 0
detector = pm.poseDetector()
lmList = []

while True:
    isTrue, frame = capture.read()
    frame = detector.findPose(frame)
    lmListPrev = lmList.copy()
    lmList = detector.findPosition(frame, draw=False)

    xsum = 0
    ysum = 0
    pointsFound = 0
    aveChange = 0

    for point in lmList:
        if point[0] in [0, 11, 12, 13, 14, 15, 16, 23, 24, 25, 26, 27, 28]:
            for prev in lmListPrev:
                if prev[0] == point[0]:
                    pointsFound += 1
                    xsum += abs(point[1]-prev[1])
                    ysum += abs(point[2]-prev[2])
                aveChange = ((xsum//pointsFound)**2+(ysum//pointsFound)**2)**(1/2)

    if len(lmList) != 0:
        cv.putText(frame, f'Speed:{aveChange:.0f}', (70, 100), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv.circle(frame, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv.putText(frame, f'FPS:{str(int(fps))}', (70, 50), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv.imshow('Video', frame)

    if cv.waitKey(10) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
