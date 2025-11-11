import cv2



def display_fisheye_feeds():
    #virtual
    #cam1 = cv2.VideoCapture("sample_fisheye1.mp4")
    #cam2 = cv2.VideoCapture("sample_fisheye2.mp4")

    cam1 = cv2.VideoCapture(0)  # Fisheye camera 1
    cam2 = cv2.VideoCapture(1)  # Fisheye camera 2

    #virtual
    # Check FPS for performance
    #fps = cam1.get(cv2.CAP_PROP_FPS)
    #print("Camera 1 FPS:", fps)
    #fps2 = cam2.get(cv2.CAP_PROP_FPS)
    #print("Camera 2 FPS:", fps2)


    while True:
        ret1, frame1 = cam1.read()
        ret2, frame2 = cam2.read()

        if ret1:
            cv2.imshow("Fisheye 1", frame1)
        if ret2:
            cv2.imshow("Fisheye 2", frame2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam1.release()
    cam2.release()
    cv2.destroyAllWindows()