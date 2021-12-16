import cv2 as cv
import time
import PoseModule as pm
import MusicModule as mm

capture = cv.VideoCapture(0)
pTime = 0
detector = pm.poseDetector()

while True:
    isTrue, frame = capture.read()
    frame = detector.findPose(frame)
    lmList = detector.findPosition(frame, draw=False)

    if len(lmList) != 0:
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
