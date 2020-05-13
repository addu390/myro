import sys

sys.path.append('../lib/')

from device_listener import DeviceListener
from pose_type import PoseType
# Servo Control
import wiringpi

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)
delay_period = 0.01


class PrintPoseListener(DeviceListener):
    def on_pose(self, pose):
        pose_type = PoseType(pose)
        print(pose_type.name)
        rotate(pose_type.name)


def rotate(name):
    if name == "FIST":
        wiringpi.pwmWrite(18, 100)

    elif name == "WAVE_OUT":
        wiringpi.pwmWrite(18, 100)
    elif name == "WAVE_IN":
        wiringpi.pwmWrite(18, 200)
    elif name == "REST":
        wiringpi.pwmWrite(18, 150)
    elif name == "FINGERS_SPREAD":
        wiringpi.pwmWrite(18, 200)
# time.sleep(delay_period)




