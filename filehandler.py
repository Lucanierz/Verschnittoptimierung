import json

def readinterm(material, dimensions, filename):
    with open(filename, 'r') as file:
        data = file.read()
    lager = json.loads(data)

    used = lager[material][dimensions]
    #print(used)
    return used

def importfile(path):
    with open(path, 'r') as file:
        data = file.read()
    return data

def exportdata(data, filename):

    f = open(filename, "w+")
    f.write(str(data))
    f.close()