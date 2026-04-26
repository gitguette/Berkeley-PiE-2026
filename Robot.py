# Device IDs
m_f = "6_10919479101575700370"
m_b = "6_7490656656070236256"

arm = "6_13086570018056326489"
claw = "4_3428342422435623147"

line = "2_10879054519292937822"

# Motors
fl_wheel = "velocity_b"
fr_wheel = "velocity_a"
bl_wheel = "velocity_a"
br_wheel = "velocity_b"

def drive(x, y, r, s):
    Robot.set_value(m_f, "invert_b", True)
    Robot.set_value(m_b, "invert_a", True)
    motors = [(y + x + r), (y - x - r), (y - x + r), (y + x - r)]
    normal = abs(max(motors, key=abs))
    if normal > 1:
        motors = [i / normal for i in motors]
    motors = [i * s for i in motors]
    Robot.set_value(m_f, fl_wheel, motors[0])
    Robot.set_value(m_f, fr_wheel, motors[1])
    Robot.set_value(m_b, bl_wheel, motors[2])
    Robot.set_value(m_b, br_wheel, motors[3])

def move_arm(speed, powermode):
    Robot.set_value(arm, "pid_enabled_a", False)
    Robot.set_value(arm, "deadband_a", 0.0)
    # Needed to hold the arm up
    base = -0.000005
    
    if powermode:
        base *= 3
        speed *= 3
    
    Robot.set_value(arm, "velocity_b", speed + base)

def calibrate():
    Robot.set_value(m_f, fl_wheel, 1.0)
    Robot.sleep(5)
    Robot.set_value(m_f, fr_wheel, 1.0)
    Robot.sleep(5)
    Robot.set_value(m_b, bl_wheel, 1.0)
    Robot.sleep(5)
    Robot.set_value(m_b, br_wheel, 1.0)
    Robot.sleep(5)

def calibrate_claw():
    Robot.set_value(claw, "servo1", 0.0)
    Robot.sleep(3)
    Robot.set_value(claw, "servo1", 0.5)
    Robot.sleep(3)
    Robot.set_value(claw, "servo1", 1.0)
    Robot.sleep(3)
    Robot.set_value(claw, "servo1", -1.0)
    Robot.sleep(3)

def linefollowmode():
    l = Robot.get_value(line, "left")
    r = Robot.get_value(line, "right")
    c = Robot.get_value(line, "center")
    
    while l > 0.3 or r > 0.3 or c > 0.3:
        diff = -0.4 * (l - r)
        drive(0, 0.3, diff, 1)
    
    drive(0, 0, 0, 0)

def autonomous():
    linefollowmode()

def teleop():
    servo = 0.5
    while True:
        if Gamepad.get_value("button_start"):
            Robot.set_value(arm, "velocity_b", 0)
            Robot.sleep(1)
            continue
        speedmult = 1.0
        if Gamepad.get_value("l_bumper"):
            speedmult = 0.5
        powermode = False
        if Gamepad.get_value("r_bumper"):
            powermode = True
        if Gamepad.get_value("button_a") and servo > -1.0:
            servo -= 0.001
        elif servo < 1.0:
            servo += 0.001
        move_arm(Gamepad.get_value("joystick_right_y") * 0.1, powermode)
        #if Gamepad.get_value("r_trigger"):
        #    servo = 0
        #else:
        #    servo = 1
        Robot.set_value(claw, "servo1", servo)
        drive(Gamepad.get_value("joystick_left_x"), Gamepad.get_value("joystick_left_y") * -1.0, Gamepad.get_value("joystick_right_x"), speedmult)