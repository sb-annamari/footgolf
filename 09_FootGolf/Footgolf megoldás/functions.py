from data import jatekos

#2. feladat, beolvasás

jatekosok = []

def beolvas(fajlnev: str) -> None:
    forras = open(fajlnev, 'r')
    for sor in forras:
        jatekosok.append(jatekos(sor.strip()))
    forras.close()


#3. feladat, játékosok száma

def osszesen() -> int:
    return len(jatekosok)

# 4. feladat, női versenyzők aránya az összes versnyzőhöz képest

def arany() -> float:
    nok = [jatekos for jatekos in jatekosok if jatekos.kategoria == 'Noi']
    arany = len(nok) / len(jatekosok) * 100
    return arany

# 5. feladat, összpontszám számítás

def osszpontszam(nev: str) -> int:
    pontszam = 0
    for jatekos in jatekosok:
        if jatekos.nev == nev:
            jatekos.pontok.sort(reverse=False)
            if jatekos.pontok[0] > 0:
                pontszam += 10
            if jatekos.pontok[1] > 0:
                pontszam += 10

            pontszam += sum(jatekos.pontok[-6:]) 
            return pontszam
        
# 6. feladat, legjobb női sportoló

def legjobb_sportolo() -> str:
    nok = [jatekos for jatekos in jatekosok if jatekos.kategoria == 'Noi']
    legjobb = nok[0]
    egyesulet = ''
    osszpont = 0
    for jatekos in nok:
        if osszpontszam(jatekos.nev) > osszpontszam(legjobb.nev):
            legjobb = jatekos
            egyesulet = jatekos.egyesulet
            osszpont = osszpontszam(jatekos.nev)
    return legjobb.nev, egyesulet, osszpont

# 7. feladat, férfi versenyzők, fájlba írás
    
def ferfiak(fajlnev: str) -> None:
    ferfiak = [jatekos for jatekos in jatekosok if jatekos.kategoria == 'Felnott ferfi']
    with open(fajlnev, 'w') as fajl:
        for jatekos in ferfiak:
            fajl.write(f'{jatekos.nev}; {osszpontszam(jatekos.nev)}\n')

#8. feladat, statisztika

def statisztika() -> dict:
    stat = {}
    for jatekos in jatekosok:
        if jatekos.egyesulet != 'n.a.':
            if jatekos.egyesulet not in stat:
                stat[jatekos.egyesulet] = 1
            else:
                stat[jatekos.egyesulet] += 1
    return stat
