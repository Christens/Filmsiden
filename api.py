import requests as req

def tilfeldig(n,søk):
    url = f"http://www.omdbapi.com/?i=tt3896198&apikey=16149be5&s={søk}"
    resultat = req.get(url, headers = {'User-Agent': 'Christen'})
    data = resultat.json()
    print(data["Search"][n]["Title"])
    return resultat

tilfeldig(0, "")