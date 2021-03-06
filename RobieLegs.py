from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import atexit


class RobieLegs:
    mh = Adafruit_MotorHAT(addr=0x60)
    leftLeg = mh.getMotor(2)
    rightLeg = mh.getMotor(1)

    def turnOffMotors(self):
        self.rightLeg.run(Adafruit_MotorHAT.RELEASE)
        self.leftLeg.run(Adafruit_MotorHAT.RELEASE)

    def roll(self, x, y):

        if y >= 0:
            self.leftLeg.run(Adafruit_MotorHAT.FORWARD)
            self.rightLeg.run(Adafruit_MotorHAT.FORWARD)
        elif y < 0:
            y = y * -1
            self.leftLeg.run(Adafruit_MotorHAT.BACKWARD)
            self.rightLeg.run(Adafruit_MotorHAT.BACKWARD)

        if x < 0:
            x = x * -1
            leftSpeed = y
            rightSpeed = y - x

            if rightSpeed < 0:
                rightSpeed = rightSpeed * -1

        elif x >= 0:
            rightSpeed = y
            leftSpeed = y - x

            if leftSpeed < 0:
                leftSpeed = leftSpeed * -1

        self.rightLeg.setSpeed(rightSpeed)
        self.leftLeg.setSpeed(leftSpeed)

atexit.register(RobieLegs().turnOffMotors)
