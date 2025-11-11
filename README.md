# Raspberry Pi Eye-Tracking Display System

---

⚠️ WARNING: USE AT YOUR OWN RISK ⚠️

This repository is provided "AS IS" and is a WORK IN PROGRESS.  
By using, downloading, or interacting with this code, you agree to the following terms:

1. **NO WARRANTY**  
   This software is provided without any guarantees or warranties, express or implied.  
   It may fail, malfunction, or behave unpredictably.

2. **POTENTIAL RISKS INCLUDE BUT ARE NOT LIMITED TO**:  
   - Hardware damage (Raspberry Pi, cameras, displays, peripherals).  
   - Software corruption, data loss, or SD card failure.  
   - Overheating, electrical hazards, or short circuits.  
   - Fire, smoke, or catastrophic hardware failure.  
   - Network instability, security vulnerabilities, or data breaches.  
   - Physical injury or property damage caused by improper wiring or usage.  
   - Complete system crashes or infinite loops consuming resources.  

3. **NO LIABILITY**  
   The author is NOT responsible for:  
   - Any direct, indirect, incidental, or consequential damages.  
   - Any loss of data, revenue, or hardware.  
   - Any personal injury, property damage, or legal consequences.  

4. **LEGAL DISCLAIMER**  
   By using this code, you agree that:  
   - You assume ALL responsibility for testing, deployment, and safety.  
   - You will NOT hold the author liable for any damages or losses.  
   - You comply with all local laws and regulations regarding electronics and software use.  

5. **NO SUPPORT OR GUARANTEE OF FUNCTIONALITY**  
   This is experimental code. It may break your computer, corrupt your files, or cause unexpected behavior.  
   If you are not comfortable with these risks, DO NOT USE THIS CODE.  

6. **LICENSE NOTICE**  
   This project currently uses a restrictive license.  
   No modification, redistribution, or commercial use is allowed until a future license change is published (planned: MIT).  

IF YOU DO NOT AGREE TO THESE TERMS, DO NOT USE THIS SOFTWARE.

---

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

