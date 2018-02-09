import Adafruit_PCA9685


class RobieEyes:
    pwmHat = Adafruit_PCA9685.PCA9685()
    pwmHat.set_pwm_freq(1000)
    
    pwmHat.set_pwm(0, 0, 1)
    pwmHat.set_pwm(1, 4096, 1)  #blue
    pwmHat.set_pwm(2, 0, 1)

    def setColor(self, channel, red, green, blue):
        red = self.translate(red)
        green = self.translate(green)
        blue = self.translate(blue)

        self.pwmHat.set_pwm(channel, red, 1)
        self.pwmHat.set_pwm((channel + 1), blue, 1)
        self.pwmHat.set_pwm((channel + 2), green, 1)

    def translate(self, value):
        valueScaled = value / 255
        return valueScaled * 4096

eye = RobieEyes()
