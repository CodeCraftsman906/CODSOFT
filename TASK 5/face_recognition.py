#--------------------------------------------------------------------
# FACE RECOGNITION AND VERIFICATION USING ArcFace
#--------------------------------------------------------------------


import cv2
from deepface import DeepFace

known_image = "known_faces/raghav.jpg"

cap = cv2.VideoCapture(0)

frame_count = 0
label = "Unknown"

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_count += 1

    try:

        if frame_count % 30 == 0:

            result = DeepFace.verify(
                img1_path=known_image,
                img2_path=frame,
                model_name="ArcFace",
                enforce_detection=False
            )

            if result["verified"]:
                label = "Raghav"
            else:
                label = "Unknown"

    except:
        label = "No Face"

    cv2.putText(
        frame,
        label,
        (50,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2    
    )

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):   
        break

cap.release()
cv2.destroyAllWindows()