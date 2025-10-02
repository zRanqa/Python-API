import random
import json

class CaravanPark:
    def __init__(self, name, contact, lat, long, rng: random.Random):
        self.name = name
        self.contact = contact
        self.lat = lat
        self.long = long

        self.sites = rng.randint(10,30)
        self.cost = rng.randint(30,100)
        self.rating = rng.randint(5,50) / 10
        
        self.isDogFriendly = rng.choice([True, False])
        self.hasEnsuites = rng.choice([True, False])

        self.hasFreeWifi = rng.choice([True, False])

        self.hasTennisCourt = rng.choice([True, False])
        self.hasBasketballCourt = rng.choice([True, False])
        self.hasSwimmingPool = rng.choice([True, False])


    def to_dict(self):
        return {
            'name': self.name,
            'contact': self.contact,
            'lat': self.lat,
            'long': self.long,
            'sites': self.sites,
            'cost': self.cost,
            'rating': self.rating,
            'isDogFriendly': self.isDogFriendly,
            'hasEnsuites': self.hasEnsuites,
            'hasTennisCourt': self.hasTennisCourt,
            'hasBasketballCourt': self.hasBasketballCourt,
            'hasSwimmingPool': self.hasSwimmingPool,
            'hasFreeWifi': self.hasFreeWifi
        }
