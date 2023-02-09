import json

def json_filmer():
    fil = open("imdb.json")
    filmer = json.load(fil)
    fil.close()
    return filmer

