import requests as req

def søk_etter_filmer(søk):
    url = f"http://www.omdbapi.com/?i=tt3896198&apikey=16149be5&s={søk}"
    resultat = req.get(url, headers = {'User-Agent': 'Christen'})
    data = resultat.json()
    svar = data["Search"]
    return svar
