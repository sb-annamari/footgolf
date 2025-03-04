class jatekos:
    def __init__(self, sor: str) -> None:
        adatok = sor.split(';')
        self.nev = adatok[0]
        self.kategoria = adatok[1]
        self.egyesulet = adatok[2]
        self.pontok = [int(adatok[i]) for i in range(3, 11)] 