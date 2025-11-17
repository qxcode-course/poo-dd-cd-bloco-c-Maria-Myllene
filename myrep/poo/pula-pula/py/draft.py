class Kid:
    def __init__ (self, name: str, age: int):
        self.__name = name
        self.__age = age

    def __str__ (self):
        return f"{self.__name}:{self.__age}"
    
    def getName (self):
        return self.__name
    
class Trampoline:
    def __init__ (self):
        self.playing: list [Kid] = []
        self.waiting: list [Kid] = []
    
    def __str__ (self):
        fila = ", ".join([str(x) for x in self.waiting])
        brincando = ", ".join(str(x) for x in self.playing)
        return f"[{fila}] => [{brincando}]"

    def arrive (self, kid: Kid):
        self.waiting.insert(0, kid)

    def enter (self):
        criança = self.waiting.pop()
        self.playing.insert(0, criança)
        del criança
    
    def leave (self):
        if self.playing == []:
            return
        kid = self.playing.pop()
        self.waiting.insert(0, kid)
        
    
    def remove (self, crianca: str):
        for kid in self.waiting:
            if kid.getName() == crianca:
                self.waiting.remove(kid)
                return
        for kid in self.playing:
            if kid.getName() == crianca:
                self.playing.remove(kid)
                return
        print(f"fail: {crianca} nao esta no pula-pula")

        
    
def main():
    trampolim = Trampoline()

    while True:
        line = input()
        args: list[str] = line.split(" ")
        print("$" + line)

        if args [0] == "end":
            break   
        elif args [0] == "arrive":
            name = args[1]
            age = int(args[2])
            fila = Kid (name, age)
            trampolim.arrive(fila)
        elif args [0] == "show":
            print(trampolim)
        elif args [0] == "enter":
            trampolim.enter()
        elif args [0] == "leave":
            trampolim.leave()
        elif args [0] == "remove":
            crianca = args[1]
            trampolim.remove(crianca)
        else: 
            print("fail: comando invalido")

main()