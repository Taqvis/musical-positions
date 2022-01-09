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

    speed = detector.findSpeed(lmListPrev, lmList)
    mm.play(speed)

    if len(lmList) != 0:
        cv.putText(frame, f'Speed:{speed:.0f}', (70, 100), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    while fps > 10:
        cTime = time.time()
        fps = 1 / (cTime - pTime)
    pTime = cTime

    cv.putText(frame, f'FPS:{str(int(fps))}', (70, 50), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv.imshow('Video', frame)

    if cv.waitKey(10) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
