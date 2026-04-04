# NOTE FROM PIE STAFF
# This code has not been tested thoroughly on robots; it is meant to be guidance to help improve
# the code you currently have. It will be tested throughout the week and will be available for you
# to use during final competition if you are unable to get working code on your testing day.
# (And yes, it is intentionally hard to use....)

# Device IDs
MOTOR1_ID = "6_10919479101575700370"
MOTOR2_ID = "6_7490656656070236256"

# Motors
LEFT_MTR = "a"
RIGHT_MTR = "b"

# Controls (change these to your preferences)
FORWARD = "w"
BACK = "s"
LEFT = "a"
RIGHT = "d"

def autonomous():
    Robot.set_value(MOTOR1_ID, "velocity_" + LEFT_MTR, 1.0)
    Robot.set_value(MOTOR2_ID, "velocity_" + RIGHT_MTR, -1.0)

def teleop():
    while True:
        if True:
            Robot.set_value(MOTOR2_ID, "velocity_" + LEFT_MTR, -1.0)
            Robot.set_value(MOTOR1_ID, "velocity_" + RIGHT_MTR, 1.0)
        elif Keyboard.get_value(BACK):
            Robot.set_value(MOTOR2_ID, "velocity_" + LEFT_MTR, 1.0)
            Robot.set_value(MOTOR1_ID, "velocity_" + RIGHT_MTR, -1.0)
        elif Keyboard.get_value(LEFT):
            Robot.set_value(MOTOR1_ID, "velocity_" + LEFT_MTR, 1.0)
            Robot.set_value(MOTOR2_ID, "velocity_" + RIGHT_MTR, -1.0)
        elif Keyboard.get_value(RIGHT):
            Robot.set_value(MOTOR1_ID, "velocity_" + LEFT_MTR, -1.0)
            Robot.set_value(MOTOR2_ID, "velocity_" + RIGHT_MTR, 1.0)
