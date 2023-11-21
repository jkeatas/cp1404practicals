from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability"""
    def __init__(self, name, fuel, reliability):
        """Initialise a unreliable car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance.

               Drive given distance if car has enough fuel and has a random number
               higher than distance or drive until fuel runs out return the distance actually driven.
               """
        if distance > randint(0, 100):
            distance = 0
        elif distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance
