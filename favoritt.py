class Favoritt:
    def __init__(self, navn):
        self._navn = navn
        self._poeng = 0

    def øk_poeng(self):
        self._poeng += 1

    def hent_poeng(self):
        return self._poeng


'''
filmer = 0
#Kode til app.py osm forhåpentligvis kan få favorittsystem til å fungere

favoritter = [] #lager en liste med objekter av alle filmene fra imdb.json
for film in filmer:
    ny_favoritt = Favoritt(film["navn"])
    favoritter.append(ny_favoritt)

def øk_favorittpoeng(filmnavn): #tar inn navn som skal komme ved å trykke på pilen ofr å like, så øke sel._poeng
    for film in favoritter:
        if film.self._navn == filmnavn:
            film.øk_poeng()
'''