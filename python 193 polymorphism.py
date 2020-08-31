class Vehicle:
    goal = "getting from point a to b"
    kind = "many ways one"
    terrain = "terrain"
    engine = "vehilcle"

    def moving(self):
        purpose = "The {} traverses {} with a {} for the purpose of {}.".format(self.kind, self.terrain, self.engine, self.goal)
        return purpose

class Boat(Vehicle):
    kind = "boat"
    terrain = "water"
    engine_boat= "outboard"
    additional_requirements = "Trailer"
    goal = "fun"
    safety = "life preservers"
    
    def fishing(self):
        fun = "The {} traverses {} with an {} motor. You just need a {} to get it to the {} and {}.".format(self.kind, self.terrain, self.engine_boat, self.additional_requirements ,self.terrain, self.safety)
        return fun

class Bicycle(Vehicle):
    kind = "mountain bike"
    terrain = "rocky"
    power = "human"
    mv_method = "wheels"
    goal = "going downhill"

    def downhill(self):
        excitement = "The {} traverses {} terrain with a {} engine and a few {}.".format(self.kind, self.terrain, self.power, self.mv_method, self.power)
        return excitement
    
if __name__ == "__main__":

    vehicle = Vehicle()
    print(vehicle.moving())
    
    boat = Boat()
    print(boat.fishing())

    bicycle = Bicycle()
    print(bicycle.downhill())
