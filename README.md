# Raspberry Pi Eye-Tracking Display System

# ⚠️ WARNING: WIP, USE AT YOUR OWN RISK
This project is **Work In Progress (WIP)**.  
**YMMV** (Your Mileage May Vary).  
It may **break your computer**, **corrupt your SD card**, or **burn everything down** (figuratively).  
I am **NOT RESPONSIBLE** for any damages, data loss, hardware failure, or any other problems caused by using this repository.  
If you choose to run this code, you do so **entirely at your own risk**.


## Description
A Raspberry Pi 5 system that streams dual fisheye camera feeds to HDMI displays while tracking eye openness in five phases and rendering animated animal eyes on two SPI screens.

## Features
- **Dual fisheye cameras** → real-time HDMI output.
- **Eye tracking** using MediaPipe and OpenCV.
- **Five eye states**: Open, 3/4 Open, Half, 3/4 Closed, Closed.
- **Two SPI displays** show animated animal eyes based on eye state.
- **Multi-threaded architecture** for smooth HDMI performance and asynchronous SPI updates.
- Includes **requirements.txt**, **requirements-dev.txt**, and **pytest import validation**.

## Hardware
- Raspberry Pi 5 (8GB recommended)
- 2 fisheye cameras (USB or CSI)
- 1 eye-tracking camera (USB or CSI)
- 2 HDMI displays
- 2 SPI displays (ST7789 or ILI9341)

## Software
- Python 3.9+
- OpenCV, MediaPipe, Pillow
- ST7789 or luma.lcd for SPI
- pytest, flake8 for validation

## Installation
```bash
git clone https://github.com/See_what_i_see_with_my_eyes.git
cd See_what_i_see_with_my_eyes
pip install -r requirements.txt
```

## Testing
```bash
pytest test_imports.py
flake8 .
python -m py_compile *.py
```

