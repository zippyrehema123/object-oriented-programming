# Base Vehicle class
class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
    
    def move(self):
        return "Moving in some way"
    
    def get_details(self):
        return f"{self.name} (Max Speed: {self.max_speed})"


# Car class inherits from Vehicle
class Car(Vehicle):
    def __init__(self, name, max_speed, wheels=4):
        super().__init__(name, max_speed)
        self.wheels = wheels
    
    def move(self):
        return f"🚗 Driving on {self.wheels} wheels at up to {self.max_speed} mph"
    
    def honk(self):
        return "Beep beep!"


# Boat class inherits from Vehicle
class Boat(Vehicle):
    def __init__(self, name, max_speed, propulsion_type):
        super().__init__(name, max_speed)
        self.propulsion_type = propulsion_type
    
    def move(self):
        return f"🚢 Sailing using {self.propulsion_type} at up to {self.max_speed} knots"
    
    def sound_horn(self):
        return "Hoooooonk!"


# Plane class inherits from Vehicle
class Plane(Vehicle):
    def __init__(self, name, max_speed, max_altitude):
        super().__init__(name, max_speed)
        self.max_altitude = max_altitude
    
    def move(self):
        return f"✈️ Flying at up to {self.max_speed} mph and altitude of {self.max_altitude} feet"
    
    def take_off(self):
        return "Preparing for takeoff!"


# Bicycle class inherits from Vehicle
class Bicycle(Vehicle):
    def __init__(self, name, max_speed, type_of_bike):
        super().__init__(name, max_speed)
        self.type_of_bike = type_of_bike
    
    def move(self):
        return f"🚲 Pedaling the {self.type_of_bike} bike at up to {self.max_speed} mph"
    
    def ring_bell(self):
        return "Ring ring!"


# Function showing polymorphism in action
def start_race(vehicles):
    print("🏁 Race Starting! 🏁")
    for vehicle in vehicles:
        print(f"{vehicle.get_details()} - {vehicle.move()}")


# Example usage
if __name__ == "__main__":
    # Create vehicles
    car = Car("Tesla Model S", 155, 4)
    boat = Boat("Speedboat", 60, "outboard motor")
    plane = Plane("Cessna 172", 188, 13500)
    bicycle = Bicycle("Mountain Bike", 25, "mountain")
    
    # Put them in a list to demonstrate polymorphism
    vehicles = [car, boat, plane, bicycle]
    
    # Show how they all implement move() differently
    start_race(vehicles)
    
    # Call class-specific methods
    print("\nVehicle-specific actions:")
    print(f"Car: {car.honk()}")
    print(f"Boat: {boat.sound_horn()}")
    print(f"Plane: {plane.take_off()}")
    print(f"Bicycle: {bicycle.ring_bell()}")