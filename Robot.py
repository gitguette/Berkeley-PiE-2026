# Device IDs
m_f = "6_10919479101575700370"
m_b = "6_7490656656070236256"

arm = "6_13086570018056326489"
claw = "4_3428342422435623147"

line = "Placeholder"

# Motors
fl_wheel = "velocity_b"
fr_wheel = "velocity_a"
bl_wheel = "velocity_a"
br_wheel = "velocity_b"

def drive(x, y, r, s):
    motors = [(x + y + r), (x - y - r), (x - y + r), (x + y - r)]
    normal = abs(max(motors, key=abs))
    if normal > 1:
        motors = [i / normal for i in motors]
    motors = [i * s for i in motors]
    Robot.set_value(m_f, fl_wheel, -1.0 * motors[0])
    Robot.set_value(m_f, fr_wheel, -1.0 * motors[1])
    Robot.set_value(m_b, bl_wheel, motors[2])
    Robot.set_value(m_b, br_wheel, motors[3])

def move_arm(speed):
    Robot.set_value(arm, "pid_enabled_b", False)
    Robot.set_value(arm, "deadband_b", 0.0)
    # Needed to hold the arm up
    base = -0.1
    
    Robot.set_value(arm, "velocity_b", speed + base)

"""
def linefollowmode():
    while Robot.get_value(line, "center") >= 0.6:
        drive(0, 1, 0, 1)
    while Robot.get_value(line, "center") < 0.6:
"""

def autonomous():

def teleop():
    while True:
        servo = 0.0
        move_arm(Gamepad.get_value("joystick_right_y") * 0.24)
        if Gamepad.get_value("button_a") and servo > 0:
            servo -= 1
        if Gamepad.get_value("button_b") and servo < 180:
            servo += 1
        Robot.set_value(claw, "servo1", servo)
        drive(Gamepad.get_value("joystick_right_x") * 0.6, Gamepad.get_value("joystick_left_y") * -1.0, 0, 1.0)