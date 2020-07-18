# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# --**base class**--
class Vehicle:
    pass

# subclass of Vehicle
class GroundVehicle(Vehicle):
    pass

# subclass of GroundVehicle, which is itself a Subclass of Vehicle
class Car(GroundVehicle):
    pass

# subclass of GroundVehicle, a subclass of Vehicle
class Motorcycle(GroundVehicle):
    pass

# subclass of Vehicle
class FlightVehicle(Vehicle):
    pass

# subclass of Flight Vehicle
class Airplane(FlightVehicle):
    pass

# subclass of Flight Vehicle
class Starship(FlightVehicle): 
    pass