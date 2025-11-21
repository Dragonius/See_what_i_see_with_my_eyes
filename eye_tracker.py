# This software is provided for "educational and experimental purposes only".
# It is "NOT intended for production use".
# By using this code, you agree that you assume "ALL risks" and the author is "NOT liable" for any damages, losses, or consequences.

import cv2
import mediapipe as mp


mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# THIS NEED TO RECALIBRED !!!!
LEFT_EYE_IDX = [33, 159, 145, 153, 154, 133]


def get_eye_state():
    # virtual
    cap = cv2.VideoCapture("./assets/eye_test_video.mp4")
    # cap = cv2.VideoCapture(2)  # Eye tracking camera
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            for landmarks in results.multi_face_landmarks:
                eye_points = [landmarks.landmark[i] for i in LEFT_EYE_IDX]
                top = eye_points[1].y
                bottom = eye_points[5].y
                ear = abs(top - bottom)

                # Map EAR to 5 phases
                if ear > 0.045:
                    return "open"
                elif ear > 0.035:
                    return "open_3_4"
                elif ear > 0.025:
                    return "half"
                elif ear > 0.015:
                    return "closed_3_4"
                else:
                    return "closed"

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
