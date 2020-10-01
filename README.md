Update: Signals from surface EMG (Electro Myography) sensors are not very reliable for certain amputees, hence considering to rely more on Inertial Measurement Unit (IMU).
Get the latest updated from the repository: https://github.com/addu390/motion-tracking-kai-python

## MYRO : MY Robotic Arm
<img src="https://pyblog.xyz/wp-content/uploads/2020/09/Myro_Final.png" width="40" > : https://myro.in

A simple library developed for my final year project : Myo Electric Prosthetic Arm

### Before using a MYO band
<img src="https://pyblog.xyz/wp-content/uploads/2020/09/three-copy.png" width="500"/>

MYO Band (https://myo.com) connected to a Raspberry pi 3 which controls a 3D printed prosthetic arm powered by servo motors.
The signals received from the MYO band is sent to the micro-processor over bluetooth, which is further processed and falls under one of the pre-defined 13 patterns such as FIST, GRAB, POINT (For finger), PINCH and several more, these patterns are specific to individual users and tweaked accordingly, as the myo signals depends on several factors of the residual arm.

![Basic block diagram](https://pyblog.xyz/wp-content/uploads/2020/02/Block-Diagram.png?raw=true)

While this library is light weight and easy, the official library from MYO: https://github.com/NiklasRosenstein/myo-python
Examples: https://github.com/NiklasRosenstein/myo-python/tree/master/examples

### Myro Android app

Arduino Nano + HC-05 bluetooth module for modularity (plug-n-play), interconnected to the Raspberry Pi 3.
<img src="https://pyblog.xyz/wp-content/uploads/2020/09/myro-app.png?raw=true" width="300"/>

Term paper: https://pyblog.xyz/wp-content/uploads/2020/09/Adesh-Nalpet-Adimurthy-Term-Paper.pdf

<img src="https://pyblog.xyz/wp-content/uploads/2020/09/adesh-hi.jpg" width="300">
#### Hi, have a look at the new developments
- IMU with KAI: https://github.com/addu390/motion-tracking-kai-python
- For more details, visit: https://myro.in
