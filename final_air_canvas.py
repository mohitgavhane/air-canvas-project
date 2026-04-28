import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

prev_x, prev_y = 0, 0
canvas = None

draw_color = (0, 255, 0)  # Default green

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    # Top color buttons
    cv2.rectangle(frame, (0, 0), (150, 65), (0, 0, 255), -1)     # Red
    cv2.rectangle(frame, (150, 0), (300, 65), (0, 255, 0), -1)   # Green
    cv2.rectangle(frame, (300, 0), (450, 65), (255, 0, 0), -1)   # Blue
    cv2.rectangle(frame, (450, 0), (640, 65), (0, 0, 0), -1)     # Eraser

    cv2.putText(frame, "RED", (40, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.putText(frame, "GREEN", (170, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.putText(frame, "BLUE", (330, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.putText(frame, "ERASER", (470, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            h, w, c = frame.shape

            x = int(handLms.landmark[8].x * w)
            y = int(handLms.landmark[8].y * h)

            middle_y = int(handLms.landmark[12].y * h)

            cv2.circle(frame, (x, y), 8, draw_color, -1)

            # Selection mode
            if y < 65:
                prev_x, prev_y = 0, 0

                if x < 150:
                    draw_color = (0, 0, 255)  # Red

                elif x < 300:
                    draw_color = (0, 255, 0)  # Green

                elif x < 450:
                    draw_color = (255, 0, 0)  # Blue

                else:
                    draw_color = (0, 0, 0)  # Eraser

            # Drawing mode
            elif y < middle_y:

                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = x, y

                thickness = 30 if draw_color == (0, 0, 0) else 5

                cv2.line(canvas,
                         (prev_x, prev_y),
                         (x, y),
                         draw_color,
                         thickness)

                prev_x, prev_y = x, y

            else:
                prev_x, prev_y = 0, 0

            mp_draw.draw_landmarks(frame,
                                   handLms,
                                   mp_hands.HAND_CONNECTIONS)

    frame = cv2.add(frame, canvas)

    cv2.imshow("Final Air Canvas", frame)

    key = cv2.waitKey(1)

    if key == ord("c"):
        canvas = np.zeros_like(frame)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()