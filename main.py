#This software is provided for "educational and experimental purposes only".
#It is "NOT intended for production use".  
#By using this code, you agree that you assume "ALL risks" and the author is "NOT liable" for any damages, losses, or consequences.

from camera_display import display_fisheye_feeds
from eye_tracker import get_eye_state
from spi_display import show_animal_eyes
import threading
import time

def run_camera_display():
    while True:
        display_fisheye_feeds()
        time.sleep(0.2)

def run_eye_tracking():
    while True:
        state = get_eye_state()
        show_animal_eyes(state)
        time.sleep(1.0)  # SPI can be slow, no problem

if __name__ == "__main__":
    t1 = threading.Thread(target=run_camera_display)
    t2 = threading.Thread(target=run_eye_tracking)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

