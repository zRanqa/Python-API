

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