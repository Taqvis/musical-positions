import cv2 as cv
import mediapipe as mp


class poseDetector():

    def __init__(self):

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose()

    def findPose(self, frame, draw=True):
        frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        self.results = self.pose.process(frameRGB)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(frame, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return frame

    def findPosition(self, frame, draw=True):
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv.circle(frame, (cx, cy), 5, (255,0,0), cv.FILLED)
        return lmList

    def findSpeed(self, lmListPrev, lmList):
        xsum = 0
        ysum = 0
        pointsFound = 0
        aveChange = 0

        for point in lmList:
            if point[0] in [0, 11, 12, 13, 14, 15, 16, 23, 24, 25, 26, 27, 28]:
                for prev in lmListPrev:
                    if prev[0] == point[0]:
                        pointsFound += 1
                        xsum += abs(point[1] - prev[1])
                        ysum += abs(point[2] - prev[2])
                    aveChange = ((xsum // pointsFound) ** 2 + (ysum // pointsFound) ** 2) ** (1 / 2)
        return aveChange