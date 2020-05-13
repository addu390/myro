import sys

sys.path.append('../lib/')

from device_listener import DeviceListener
from pose_type import PoseType
# Servo Control
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# set to be a PWM output
servoPin1 = 12
servoPin2 = 13
servoPin3 = 15
servoPin4 = 16
servoPin5 = 18

GPIO.setup(servoPin1, GPIO.OUT)
GPIO.setup(servoPin2, GPIO.OUT)
GPIO.setup(servoPin3, GPIO.OUT)
GPIO.setup(servoPin4, GPIO.OUT)
GPIO.setup(servoPin5, GPIO.OUT)

p1 = GPIO.PWM(servoPin1, 50)
p2 = GPIO.PWM(servoPin2, 50)
p3 = GPIO.PWM(servoPin3, 50)
p4 = GPIO.PWM(servoPin4, 50)
p5 = GPIO.PWM(servoPin5, 50)

p1.start(7)
p2.start(7)
p3.start(7)
p4.start(7)
p5.start(7)


class PrintPoseListener(DeviceListener):
    def on_pose(self, pose):
        pose_type = PoseType(pose)
        print(pose_type.name)
        rotate(pose_type.name)


def rotate(name):
    if name == "FIST":
        p1.ChangeDutyCycle(11)
        p2.ChangeDutyCycle(11)
        p3.ChangeDutyCycle(11)
        p4.ChangeDutyCycle(11)
        p5.ChangeDutyCycle(11)

    elif name == "WAVE_OUT":
        p1.ChangeDutyCycle(11)
        p2.ChangeDutyCycle(2)
        p3.ChangeDutyCycle(2)
        p4.ChangeDutyCycle(2)
        p5.ChangeDutyCycle(11)

    elif name == "WAVE_IN":
        p1.ChangeDutyCycle(2)
        p2.ChangeDutyCycle(11)
        p3.ChangeDutyCycle(11)
        p4.ChangeDutyCycle(2)
        p5.ChangeDutyCycle(2)

    elif name == "REST":
        p1.ChangeDutyCycle(2)
        p2.ChangeDutyCycle(2)
        p3.ChangeDutyCycle(2)
        p4.ChangeDutyCycle(2)
        p5.ChangeDutyCycle(2)

    elif name == "FINGERS_SPREAD":
        p1.ChangeDutyCycle(2)
        p2.ChangeDutyCycle(11)
        p3.ChangeDutyCycle(11)
        p4.ChangeDutyCycle(11)
        p5.ChangeDutyCycle(11)

# time.sleep(delay_period)




