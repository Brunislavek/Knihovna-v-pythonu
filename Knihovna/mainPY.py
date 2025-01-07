from KnihaPY import Kniha
from KnihovnaPY import Knihovna
from ClovekPY import Uzivatel


vl_vlak: Kniha = Kniha ("Velký vlak", "Pepa Bořič", 2000)
kn_dl_trat: Kniha = Kniha("Dlouhá trať", "Pepa Bořič", 2016)
m_domecek: Kniha = Kniha("Malý domeček", "Pepa Bořič", 2020)
kn_kr_chvile: Kniha = Kniha("Krátká chvíle", "Nikol Suchá", 2022)
podz_bunkr: Kniha = Kniha("Podzemní bunkr", "Nikol Suchá", 2023)

adela: Uzivatel = Uzivatel("Adéla Raunerová", 20, [kn_dl_trat])

kni: Knihovna = Knihovna([kn_dl_trat, kn_kr_chvile, vl_vlak,m_domecek, podz_bunkr],
                         [adela])


# foreach
for kniha in kni.seznam_knih:
    print(kniha)

print("----------------------------------------")   
    
print(adela)

print("----------------------------------------")   

knihy: list[Kniha]= kni.vyhledej_dle_nazvu("Podzemní bunkr", False)

for kniha in knihy:
    print(kniha)
    
print("----------------------------------------")   

knihy1: list[Kniha] = kni.vyhledej_dle_autor("Pepa Bořič", False)

for kniha in knihy1:
    print(kniha)
    
print("----------------------------------------")   

knihy2: list[Kniha] = kni.vyhledej_dle_roku(2016, False)

for kniha in knihy2:
    print(kniha)