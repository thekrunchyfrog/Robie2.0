import Adafruit_PCA9685


class RobieEyes:
    pwmHat = Adafruit_PCA9685.PCA9685()
    pwmHat.set_pwm_freq(1000)

    def setColor(self, channel, red, green, blue):
        red = self.translate(red)
        green = self.translate(green)
        blue = self.translate(blue)

        self.pwmHat.set_pwm(channel, red, 1)
        self.pwmHat.set_pwm((channel + 1), blue, 1)
        self.pwmHat.set_pwm((channel + 2), green, 1)

    def translate(self, value):
        value = (value - 255) * -1  # convertion for common anode led
        valueScaled = value / 255
        return valueScaled * 4096

    def blankEyes(self):
        self.pwmHat.set_pwm(0, 4096, 0)
        self.pwmHat.set_pwm(1, 4096, 0)
        self.pwmHat.set_pwm(2, 4096, 0)

        self.pwmHat.set_pwm(3, 4096, 0)
        self.pwmHat.set_pwm(4, 4096, 0)
        self.pwmHat.set_pwm(5, 4096, 0)


eye = RobieEyes().setColor(0, 255, 0, 0)
