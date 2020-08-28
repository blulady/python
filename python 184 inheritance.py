

class Bicycle:
    def __init__(self, name, wheel_numbers, brake_type, gear_number):
        self.name = name
        self.wheel_numbers = wheel_numbers
        self.brake_type = brake_type
        self.gear_number = gear_number


    

bicycle = Bicycle('single speed', '2', 'rim brake', 'free wheel')
print(bicycle.name)
print(bicycle.brake_type)

class Motorcycle(Bicycle):
    accelerate = "throttle"
    motor = "gas"


class Outdoor_Elliptical(Bicycle):
    position = "standing"
    pedals = "elliptical"


