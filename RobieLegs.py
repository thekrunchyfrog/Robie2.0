from Adafruit_MotorHAT import Adafruit_MotorHAT


import atexit


class RobieLegs:
    mh = Adafruit_MotorHAT(addr=0x60)
    leftLeg = mh.getMotor(1)
    rightLeg = mh.getMotor(2)

    def turnOffMotors(self):
        self.mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

    def roll(self, x, y):



        if y >= 0:
            self.leftLeg.run(Adafruit_MotorHAT.FORWORD)
            self.rightLeg.run(Adafruit_MotorHAT.FORWORD)
        elif y < 0:
            self.leftLeg.run(Adafruit_MotorHAT.BACKWORD)
            self.rightLeg.run(Adafruit_MotorHAT.BACKWORD)



#atexit.register(RobieLegs.turnOffMotors)
