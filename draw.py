import cv2
import mediapipe as mp
import numpy as np

# Mediapipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Camera start
cap = cv2.VideoCapture(0)

# Previous finger position
prev_x, prev_y = 0, 0

# Empty canvas
canvas = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Mirror view
    frame = cv2.flip(frame, 1)

    # Create canvas once
    if canvas is None:
        canvas = np.zeros_like(frame)

    # Convert image
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    # Detect hand
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            h, w, c = frame.shape

            # Landmark 8 = index fingertip
            x = int(handLms.landmark[8].x * w)
            y = int(handLms.landmark[8].y * h)

            # Draw circle on fingertip
            cv2.circle(frame, (x, y), 8, (255, 0, 255), -1)

            # First point setup
            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = x, y

            # Draw line
            cv2.line(canvas, (prev_x, prev_y), (x, y), (0, 255, 0), 5)

            prev_x, prev_y = x, y

    # Merge frame + canvas
    frame = cv2.add(frame, canvas)

    cv2.imshow("Air Canvas", frame)

    # ESC to exit
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()