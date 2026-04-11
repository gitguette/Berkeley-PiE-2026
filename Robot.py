# Device IDs
MTR_R = "6_10919479101575700370"
MTR_L = "6_7490656656070236256"

# Motors
MTR_F = "a"
MTR_B = "b"

# Placeholder autonomous code, drive in a loop
def autonomous():
    while True:
        apply_z_velocity(1.0)
        apply_x_velocity(1.0)
        Robot.sleep(0.5)
        apply_z_velocity(-1.0)
        apply_x_velocity(1.0)
        Robot.sleep(0.5)
        apply_z_velocity(-1.0)
        apply_x_velocity(-1.0)
        Robot.sleep(0.5)
        apply_z_velocity(1.0)
        apply_x_velocity(-1.0)
        Robot.sleep(0.5)

# 1.0: full forward, -1.0: full backward
def apply_z_velocity(value):
    Robot.set_value(MTR_L, "velocity_" + MTR_F, value * 1.0)
    Robot.set_value(MTR_R, "velocity_" + MTR_B, value * -1.0)


# 1.0: full right, -1.0: full left
def apply_x_velocity(value):
    Robot.set_value(MTR_L, "velocity_" + MTR_B, value * 1.0)
    Robot.set_value(MTR_R, "velocity_" + MTR_F, value * -1.0)

def teleop():
    while True:
        apply_z_velocity(Gamepad.get_value("joystick_left_y"))
        apply_x_velocity(Gamepad.get_value("joystick_left_x"))