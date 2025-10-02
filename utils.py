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
        case 'hasEnsuites':
            return "Ensuites"
        case 'hasTennisCourt':
            return "Tennis Court"
        case 'hasBasketballCourt':
            return "Basketball Court"
        case 'hasSwimmingPool':
            return "Swimming Pool"
        case 'hasFreeWifi': 
            return "Free Wifi"
    
    return ""


def filterNameToAppleImageName(name):
    
    match name:
        case "isDogFriendly":
            return "dog.circle"
        case "hasEnsuites":
            return "house.circle"
        case "hasBasketballCourt":
            return "basketball.circle"
        case "hasSwimmingPool":
            return "figure.pool.swim.circle"
        case "hasTennisCourt":
            return "tennis.racket.circle"
        case "hasFreeWifi":
            return "wifi.circle"
        
    return ""
    