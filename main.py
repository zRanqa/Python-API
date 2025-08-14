from flask import Flask
import json
from caravan_park import CaravanPark
import random

app = Flask(__name__)

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

@app.route('/')
def index():
    return "hello!"

@app.route('/caravan-parks/')
def getCaravanParks():
    caravanParkList = getAllCaravanParks()

    output = getDict(caravanParkList)
    return {"data" : output}

@app.route('/caravan-parks/filters/')
def getFilter():
    caravanParkList = getAllCaravanParks()
    filtersDict = caravanParkList[0].to_dict()
    filtersDict.pop("name")
    filtersDict.pop("contact")
    filtersDict.pop("lat")
    filtersDict.pop("long")
    filters = list(filtersDict.keys())
    print(filters)
    return {"data": filters}

@app.route('/caravan-parks/<filter>/')
def getCaravanParksByFilter(filter):
    caravanParkList = getAllCaravanParks()
    filteredParks = []
    for park in caravanParkList:
        if hasattr(park, filter) and getattr(park, filter):
            filteredParks.append(park.to_dict())
    return {"data": filteredParks}


if __name__ == '__main__':
    app.run(debug=True)