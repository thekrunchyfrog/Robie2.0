import Adafruit_PCA9685


class RobieEyes:
    pwmHat = Adafruit_PCA9685.PCA985()
    pwmHat.set_pwm_freq(100)

    def setColor(self, channel, red, green, blue):
        red = self.translate(red)
        green = self.translate(green)
        blue = self.translate(blue)

        self.set_pwm(channel, red, 1)
        self.set_pwm((channel + 1), blue, 1)
        self.set_pwm((channel + 2), green, 1)

    def translate(value):
        valueScaled = value / 255
        return valueScaled * 4096
