from PIL import Image
import ST7789  # or ILI9341 depending on your SPI display

#virtual
#def show_animal_eye(state):
 #   print(f"SPI Display would show: {state}")



# Initialize two displays
display_left = ST7789.ST7789(cs=8, dc=25, rst=27)
display_right = ST7789.ST7789(cs=7, dc=24, rst=23)

display_left.init()
display_right.init()

def show_animal_eyes(state):
    img_map = {
        "open": "assets/eye_open.png",
        "open_3_4": "assets/eye_open_3_4.png",
        "half": "assets/eye_half.png",
        "closed_3_4": "assets/eye_closed_3_4.png",
        "closed": "assets/eye_closed.png"
    }

    img = Image.open(img_map[state])
    display_left.display(img)
    display_right.display(img)

