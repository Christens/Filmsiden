class Favoritt:
    def __init__(self, navn):
        self._navn = navn
        self._poeng = 0
        self._plass = 0

    def øk_poeng(self):
        self._poeng += 1

    def hent_poeng(self):
        return self._poeng
    
    def hent_navn(self):
        return self._navn

    def oppdater_plass(self, plass):
        self._plass = plass