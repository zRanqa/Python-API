from caravan_park import CaravanPark
import json
import random


def getJSON():
    file = open("caravan_park_data.json")
    data = json.load(file)
    return data

def getAllCaravanParks() -> list[CaravanPark]:
    data = getJSON()
    caravanParkList = []

    randSeed = 10
    rng = random.Random(randSeed)

    for park in data:
        newCaravan = CaravanPark(park["name"], park["contact"], park["lat"], park["long"], rng)
        caravanParkList.append(newCaravan)

    return caravanParkList


def getDict(caravanParkList: list[CaravanPark]):
    newList = []
    for caravanPark in caravanParkList:
        newList.append(caravanPark.to_dict())
    return newList

def getDescFromName(name):

    match name:
        case "isDogFriendly":
            return "Dog Friendly"
        case 'hasEnsuiteSites':
            return "Ensuite"
        case 'hasPoweredSites':
            return "Powered"
        case 'hasCabins':
            return "Cabins"
        case 'lakeside':
            return "Lakeside"
        case 'hasTennisCourt':
            return "Tennis Court"
        case 'hasBasketballCourt':
            return "Basketball Court"
        case 'hasPlayground': 
            return "Playground"
    
    return ""