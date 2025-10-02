import random
import json

class CaravanPark:
    def __init__(self, name, contact, lat, long, rng):
        self.name = name
        self.contact = contact
        self.lat = lat
        self.long = long

        self.sites = rng.randint(10,30)
        self.cost = rng.randint(30,100)
        self.rating = rng.randint(5,50) / 10
        
        self.isDogFriendly = rng.choice([True, False])
        self.hasEnsuiteSites = rng.choice([True, False])
        self.hasPoweredSites = rng.choice([True, False])
        self.hasCabins = rng.choice([True, False])

        self.lakeside = rng.choice([True, False])

        self.hasTennisCourt = rng.choice([True, False])
        self.hasBasketballCourt = rng.choice([True, False])
        self.hasPlayground = rng.choice([True, False])


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
            'hasEnsuiteSites': self.hasEnsuiteSites,
            'hasPoweredSites': self.hasPoweredSites,
            'hasCabins': self.hasCabins,
            'lakeside': self.lakeside,
            'hasTennisCourt': self.hasTennisCourt,
            'hasBasketballCourt': self.hasBasketballCourt,
            'hasPlayground': self.hasPlayground
        }
