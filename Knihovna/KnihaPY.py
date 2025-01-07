Class Kniha:
    def __init__(self, nazev:str, autor:str, vydani:int) -> None:
        self.nazev:str = nazev
        self.autor:str = autor
        self.rok_vydani:int = vydani
        self.je_vypujcena:bool = False
        
    
    def __str__(self) -> str:
        return f"[{self.nazev}] ({self.autor} - {self.rok_vydani})"
    
    
        
    
