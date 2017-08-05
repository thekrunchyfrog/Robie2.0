def roll(x, y):

        if y >= 0:
            rightDir = "Forward"
            leftDir = "Forword"
        elif y < 0:
            y = y * -1
            rightDir = "Backward"
            leftDir = "Backward"

        if x < 0:
            x = x * -1
            leftSpeed = y
            rightSpeed = y - x

            if rightSpeed < 0:
                rightSpeed = rightSpeed * -1

        elif x > 0:
            rightSpeed = y
            leftSpeed = y - x

            if leftSpeed < 0:
                leftSpeed = leftSpeed * -1

        print("Right " + rightDir + " " + str(rightSpeed))
        print("Left " + leftDir + " " + str(leftSpeed))

roll(200, 30)
