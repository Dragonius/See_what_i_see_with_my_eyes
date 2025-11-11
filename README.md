# Raspberry Pi Eye-Tracking Display System

---

⚠️ WARNING: WORK IN PROGRESS – USE AT YOUR OWN RISK ⚠️

This repository and all associated files, code, and documentation are provided "AS IS" without any warranty, express or implied.  
By accessing, downloading, or using this code, you acknowledge and agree to the following:

1. **NO GUARANTEE OF FUNCTIONALITY**  
   This project is incomplete and experimental.
   It may not work as intended, may fail unexpectedly, or may produce incorrect results.
   This software is provided without any guarantees or warranties, express or implied.  
   It may fail, malfunction, or behave unpredictably.

2. **POTENTIAL RISKS**  
   - May cause system instability, crashes, or data loss.
   - May corrupt SD cards, storage devices, or operating systems.
   - May overheat or damage hardware components.
   - May result in electrical hazards if wired incorrectly.
   - May lead to unpredictable behavior including infinite loops, resource exhaustion, or network issues.
   - Hardware damage (Raspberry Pi, cameras, displays, peripherals).  
   - Software corruption, data loss, or SD card failure.  
   - Overheating, electrical hazards, or short circuits.  
   - Fire, smoke, or catastrophic hardware failure.  
   - Network instability, security vulnerabilities, or data breaches.  
   - Physical injury or property damage caused by improper wiring or usage.  
   - Complete system crashes or infinite loops consuming resources. 

3. **NO LIABILITY**  
   The author assumes **NO RESPONSIBILITY** for:
   - Hardware damage (including Raspberry Pi, displays, cameras, or peripherals).
   - Software corruption or data loss.
   - Personal injury, fire, electrical shock, or property damage.  
   - Any loss of data, revenue, or hardware.  
   - Any personal injury, property damage, or legal consequences. 
   - Any direct, indirect, incidental, or consequential damages arising from use of this code.

4. **NO SUPPORT OR WARRANTY OR GUARANTEE OF FUNCTIONALITY**
   This is experimental code.
   It may break your computer, corrupt your files, or cause unexpected behavior.  
   This code is provided without any guarantee of support, updates, or bug fixes.  
   Use at your own discretion and risk.
   If you are not comfortable with these risks, DO NOT USE THIS CODE.  

5. **LEGAL DISCLAIMER**  
   By using this repository, you agree that:
   - You will not hold the author liable for any damages or losses.
   - You assume full responsibility for testing, deployment, and safety precautions.
   - You comply with all local laws and regulations regarding electronics and software use.

6. **FUTURE LICENSE CHANGE**  
   This project currently uses a restrictive license.  
   A permissive license (e.g., MIT) may be applied in the future, but until then, all restrictions remain in effect.

IF YOU DO NOT AGREE TO THESE TERMS, DO NOT USE THIS CODE.

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

