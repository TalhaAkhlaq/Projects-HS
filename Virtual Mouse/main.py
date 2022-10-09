import cv2
import mediapipe as mp
import pyautogui
    # import numpy as np
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
     # index_x = 0
     # index_y = 0
     # middle_x = 0
     # middle_y = 0
     # ring_x = 0
     # ring_y = 0
     # pinky_x = 0
     # pinky_y = 0
     # thumb_x = 0
     # thumb_y = 0
     # index_tip_x = 0
     # index_tip_y = 0
     # middle_tip_x = 0
     # middle_tip_y = 0
     # ring_tip_x = 0
     # ring_tip_y = 0
     # pinky_tip_x = 0
     # pinky_tip_y = 0
     # thumb_tip_x = 0 
     # thumb_tip_y = 0
     # index_cmc_x = 0
     # index_cmc_y = 0
     # middle_cmc_x = 0
     # middle_cmc_y = 0
     # ring_cmc_x = 0
     # ring_cmc_y = 0
     # pinky_cmc_x = 0
     # pinky_cmc_y = 0
     # thumb_cmc_x = 0
     # thumb_cmc_y = 0
     # index_mcp_x = 0
     # index_mcp_y = 0
     # middle_mcp_x = 0
     # middle_mcp_y = 0
     # ring_mcp_x = 0
     # ring_mcp_y = 0
     # pinky_mcp_x = 0
     # pinky_mcp_y = 0
     # thumb_mcp_x = 0
     # thumb_mcp_y = 0
     # index_pip_x = 0
     # index_pip_y = 0
     # middle_pip_x = 0
     # middle_pip_y = 0
     # ring_pip_x = 0
     # ring_pip_y = 0
     # pinky_pip_x = 0
     # pinky_pip_y = 0
     # thumb_pip_x = 0
     # thumb_pip_y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y

                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    print('outside', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)
                    elif abs(index_y - thumb_y) < 100:
                        pyautogui.moveTo(index_x, index_y)
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)