# Algorithm which are followed to perform the opeartions
# 1. Find hand land marks
# 2. Get the tip of the index and middle fingure
# 3. check which fingers are up
# 4. only Index Finger : Moving Mode
# 5. convert Coordinates
# 6. smoothen Values
# 7. Move House
# 8. Both Index and Middle finger are up: Clicking Mode
# 9. find the distance Between finger
# 10. Click mouse if Distance
# 11. Frame Rate
# 12. display

# import packages
import cv2
import numpy as np
import HandtrackingModule as htm
import time
import autopy

# declare same based variables
wCam, hCam = 640, 480
frameR = 100  # Frame reduction
smoothening = 5

# previous location and current location of X and Y variable Declarations
pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

# capture Webcam output
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# detect hand landmarks
detector = htm.handDetector(maxHands=1)


wScr, hScr = autopy.screen.size()
# print(wScr, hScr)


while True:
    # 1. Find hand land marks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    # 2. Get the tip of the index and middle fingure
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        # print(x1, y1, x2, y2)

        # 3. check which fingers are up
        fingers = detector.fingersUp()

        cv2.rectangle(img,
                      (frameR, frameR),
                      (wCam - frameR, hCam - frameR),
                      (255, 20, 255),
                      2)
        # print(fingers)

        # 4. only Index Finger : Moving Mode
        if fingers[1] == 1 and fingers[2] == 0:
            # 5. convert Coordinates
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            # 6. smoothen Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (x3 - plocY) / smoothening

            # 7. Move House
            autopy.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

        # 8. Both Index and Middle finger are up: Clicking Mode
        if fingers[1] == 1 and fingers[2] == 1:

            # 9. find the distance Between finger
            length, img, lineInfo = detector.findDistance(8, 12, img)
            print(length)

            # 10. Click mouse if Distance
            if length < 30:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()

    # 11. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img,
                str(int(fps)),
                (20, 50),
                cv2.FONT_HERSHEY_PLAIN,
                3,
                (255, 0, 0),
                3)

    # 12 display
    cv2.imshow('Image', img)
    cv2.waitKey(1)
