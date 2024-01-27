import cv2
import mediapipe as mp
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

cam = cv2.VideoCapture(0)
mp_hand = mp.solutions.hands
hands_mark = mp.solutions.hands.Hands(min_detection_confidence=0.5,
        min_tracking_confidence=0.5)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks = True)
# mp_holistic = mp.solutions.holistic
# holistic_model = mp_holistic.Holistic(
#         min_detection_confidence=0.5,
#         min_tracking_confidence=0.5
#     )


while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hands_mark.process(rgb_frame)
    
    rgb_frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)
    if output.multi_hand_landmarks:
        for hand_landmarks in output.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                rgb_frame,
                hand_landmarks, mp_hand.HAND_CONNECTIONS
            )
    # landmark_point = output.multi_face_landmarks
    # landmark_point = output.multi_hand_landmarks
    # print(landmark_point)

    # results = holistic_model.process(rgb_frame)
    # mp_drawing.draw_landmarks(
    #   rgb_frame, 
    # #   results.multi_hand_landmarks, 
    #   results.left_hand_landmarks, 
    #   mp_holistic.HAND_CONNECTIONS
    # )


    cv2.imshow('hand_mouse', rgb_frame)
    cv2.waitKey(1)