import cv2
import mediapipe as mp
import pyautogui



faceMesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

screenW, screenH = pyautogui.size()
cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    imgH, imgW, _ = img.shape
    rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    output = faceMesh.process(rgbImg)
    landmarksPoints = output.multi_face_landmarks
    if landmarksPoints:
        landmarks = landmarksPoints[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x, y = int(landmark.x * imgW), int(landmark.y * imgH)
            cv2.circle(img, (x,y), 3, (0,255,255))
            if id==1:
                screenX = screenW / imgW * x
                screenY = screenH / imgH * y
                pyautogui.moveTo(screenX, screenY)

            left = [landmarks[145], landmarks[159]]
            for landmark in left:
                x, y = int(landmark.x * imgW), int(landmark.y * imgH)
                cv2.circle(img, (x,y), 3, (0,255,255))
            if (left[0].y - left[1].y) < 0.004:
                print('yes')
                pyautogui.click()
                #pyautogui.sleep(1)


    cv2.imshow('Img', img)

    key = cv2.waitKey(1)
    if key== 27:
        break

cap.release()
cv2.destroyAllWindows()
