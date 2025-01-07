from KnihaPY import Kniha
from ClovekPY import Uzivatel

class Knihovna:
    def __init__(self, knihy:list[Kniha], uzivatele: list[Uzivatel]) -> None:
        self.seznam_knih:list[Kniha] = knihy
        self.uzivatele:list[Uzivatel] = uzivatele
        self.max_pocet_vypujcenych_knih:int = 3
        
    
    def vyhledej_dle_nazvu(self, nazev:str, jen_nevypujcene: bool)-> list[Kniha]:
        knihy: list[Kniha] = []
        
        for kniha in self.seznam_knih:
            if kniha.nazev == nazev:
                if jen_nevypujcene and not kniha.je_vypujcena or not jen_nevypujcene:
                    knihy.append(kniha)
                
        return knihy
        
        
    def vyhledej_dle_autor(self, autor:str, jen_nevypujcene: bool)-> list[Kniha]:
        knihy: list[Kniha] = []
        for kniha in self.seznam_knih:
            if kniha.autor == autor:
                if jen_nevypujcene and not kniha.je_vypujcena or not jen_nevypujcene:
                    knihy.append(kniha)
                
        return knihy
        
        
    def vyhledej_dle_roku(self, rok_vydani:int, jen_nevypujcene: bool)-> list[Kniha]:
        knihy: list[Kniha] = []
        for kniha in self.seznam_knih:
            if kniha.rok_vydani > rok_vydani:
                if jen_nevypujcene and not kniha.je_vypujcena or not jen_nevypujcene:
                    knihy.append(kniha)
                
        return knihy
    

    