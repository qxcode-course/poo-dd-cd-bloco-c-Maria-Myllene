class Grafite:
    def __init__ (self, calibre: float, dureza: str, tamanho: int):
        self.__calibre = calibre 
        self.__dureza = dureza
        self.__tamanho = tamanho

    def __str__ (self):
        return f"{self.__calibre}:{self.__dureza}:{self.__tamanho}"