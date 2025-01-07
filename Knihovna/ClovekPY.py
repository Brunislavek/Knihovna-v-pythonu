from __future__ import annotations
from KnihaPY import Kniha


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from KnihovnaPY import Knihovna

class Uzivatel:
    def __init__(self, jmeno:str, vek:int, vypujcene_knihy:list[Kniha]) -> None:
        self.jmeno:str = jmeno
        self.vek:int = vek
        self.vypujcene_knihy:list[Kniha] = vypujcene_knihy
        
    
    
    def __str__(self) -> str:
        r: str = ", ".join([kniha.nazev for kniha in self.vypujcene_knihy])
        
    #    r: str = ""
    #    for i in range(len(self.vypujcene_knihy)):
    #        r += self.vypujcene_knihy[i].nazev
    #        if i < len(self.vypujcene_knihy) -1:
    #            r += ", "
    
    
        return f"({self.jmeno}) [{len(self.vypujcene_knihy)} knih]: {r}"
    
    def vypujcit_knihu(self, nazev:str, knihovna:Knihovna):
        from KnihovnaPY import Knihovna
        print(knihovna.max_pocet_vypujcenych_knih)
        return True
    