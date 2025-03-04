from functions import *

#2. feladat, beolvasás

beolvas('fob2016.txt')

#ellenőrzés
#for ja in jatekosok:
#    print(ja.pontok)

#3. feladat, játékosok száma

print(f'3. feladat: Versenyzők száma {osszesen()}')

#4. feladat, női versenyzők aránya az összes versnyzőhöz képest

print(f'4. feladat: A női versenyzők aránya: {arany():.2f}%')

#5. feladat, összpontszám számítás  -  Példa: megadott játékos összpontszáma

versenyzo = osszpontszam('Bacskai Bence')
print(f'5. feladat: A megadott játékos összpontszáma: {versenyzo}')

#6. feladat, legjobb női sportoló

nev, egyesulet, osszpont = legjobb_sportolo()
print(f'6. feladat: A bajnok női versenyző: \n\tNév:{nev}\n\tEgyesület: {egyesulet}\n\tÖsszpont: {osszpont}')


#7. feladat, férfi versenyzők, fájlba írás

ferfiak('osszpontFF.txt')

#8. feladat, statisztika

stat = statisztika()
print('8. feladat: Egyesület statisztika:')
for key, value in stat.items():
    if value >= 3:
        print(f'\t{key} - {value} fő')