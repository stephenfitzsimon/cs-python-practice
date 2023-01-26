# Define the DriveBot class here!
class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = 999999
    robot_count = 0

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.control_bot(10, 180)
robot_1.adjust_sensor(20)

robot_2 = DriveBot(35, 75, 25)

robot_3 = DriveBot()

DriveBot.latitude = -50.0
DriveBot.longitude = 50.0
DriveBot.all_disabled = True

print(robot_1.id)
print(robot_2.id)
print(robot_3.id)