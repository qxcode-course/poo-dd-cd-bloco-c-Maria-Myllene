class Lead:
    def __init__ (self, thickness: float, hardness: str, size: int):
        self.__thickness: float = thickness
        self.__hardness: str = hardness
        self.__size: int = size

    def __str__ (self):
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"
    
    def getThickness (self):
        return self.__thickness

class Pencil:
    def __init__(self, calibre: float, bico: Lead | None):
        self.calibre =  None
        self.bico = None
        self.barrel: list[Lead] = []

    def initLapiseira(self, tamanho: float):
        self.calibre = tamanho
        return True
    
    def __str__ (self):
        bico ="[]" if self.bico is None else f"[{self.bico}]"
        if self.barrel == []:
            tambor = "<>"
        else:
            pontas = "".join(str(x) for x in self.barrel)
            tambor = f"<{pontas}>"
        return f"calibre: {self.calibre}, bico: {bico}, tambor: {tambor}"
    
    def insert (self, grafite: Lead):
        if self.calibre != grafite.getThickness():
            print("fail: calibre incompatível")
            return
        self.barrel.append(grafite)

def main():
    lapiseira = Pencil(0.0, None)

    while True:
        line = input()
        args: list[str] = line.split(" ")
        print("$" + line)

        if args [0] == "end":
            break
        elif args [0] == "init":
            tamanho = float(args[1])
            lapiseira.initLapiseira(tamanho)
        elif args [0] == "show":
            print(lapiseira)
        elif args [0] == "insert":
            thickness = float(args[1])
            hardness = args[2]
            size = int(args[3])
            grafite = Lead(thickness, hardness, size)
            lapiseira.insert(grafite)
        else:
            print("fail: comando invalido")

main()