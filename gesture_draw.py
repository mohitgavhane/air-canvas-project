import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

prev_x, prev_y = 0, 0
canvas = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            h, w, c = frame.shape

            # Index fingertip
            x = int(handLms.landmark[8].x * w)
            y = int(handLms.landmark[8].y * h)

            # Middle fingertip
            middle_y = int(handLms.landmark[12].y * h)

            # Draw fingertip circle
            cv2.circle(frame, (x, y), 8, (255, 0, 255), -1)

            # Condition:
            # If index finger is above middle finger → draw
            if y < middle_y:

                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = x, y

                cv2.line(canvas, (prev_x, prev_y), (x, y), (0, 255, 0), 5)

                prev_x, prev_y = x, y

            else:
                prev_x, prev_y = 0, 0

            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

    frame = cv2.add(frame, canvas)

    cv2.imshow("Gesture Air Canvas", frame)

    key = cv2.waitKey(1)

    # Press C to clear screen
    if key == ord("c"):
        canvas = np.zeros_like(frame)

    # ESC to exit
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()