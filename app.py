from flask import Flask, request
import utils

app = Flask(__name__)


@app.route('/')
def index():
    return "hello!"

# TRY: /caravan-parks?isDogFriendly=true&hasEnsuiteSites=true
@app.route('/caravan-parks/')
def getCaravanParks():
    query_params = request.args
    print(query_params)

    caravanParkList = utils.getAllCaravanParks()
    filteredParks = []
    for caravanPark in caravanParkList:
        ignorePark = False
        for key,value in query_params.items():
            if not (hasattr(caravanPark, key) and getattr(caravanPark, key)) and value.lower() == "true":
                ignorePark = True
                break
        if not ignorePark:
            filteredParks.append(caravanPark)

    return {"data" : utils.getDict(filteredParks)}

@app.route('/caravan-parks/filters/')
def getFilter():
    caravanParkList = utils.getAllCaravanParks()
    if len(caravanParkList) == 0:
        return {"data": []}
    filtersDict = caravanParkList[0].to_dict()
    filtersDict.pop("name")
    filtersDict.pop("contact")
    filtersDict.pop("lat")
    filtersDict.pop("long")
    filters = list(filtersDict.keys())
    filterDesc = []
    for filter in filters:
        filterDesc.append({"name": filter, "desc": utils.getDescFromName(filter)})
    return {"data": filterDesc}


if __name__ == '__main__':
    app.run(debug=True)