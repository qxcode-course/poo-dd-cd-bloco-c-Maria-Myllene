class Client:
    def __init__ (self, nome: str):
        self.__nome: str = nome

    def __str__ (self):
        return f"{self.__nome}"

    def getCliente (self):
        return self.__nome


class Market:
    def __init__ (self, caixas: int):
        self.counters: list[Client | None] = []
        for i in range(caixas):
            self.counters.append(None)
        self.wainting: list[Client] = []
    
    def __str__ (self):
        caixas = ", ".join(["-----" if x == None else str(x) for x in self.counters])
        espera = ", ".join([str(x) for x in self.wainting])
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"
    
    def arrive (self, pessoa: Client):
        self.wainting.append(pessoa)

    def call (self, index: int):
        if self.wainting == []:
            print("fail: sem clientes")
            return
        if self.counters[index] != None:
            print("fail: caixa ocupado")
            return
        self.counters[index] = self.wainting[0]
        del self.wainting [0]
    
    def finish (self, index: int):
        if index < 0 or index >= len(self.counters):
            print("fail: caixa inexistente")
            return
        if self.counters[index] == None:
            print("fail: caixa vazio")
            return
        self.counters[index] = None

def main():
    budega = Market (0)

    while True:
        line = input()
        args: list[str] = line.split(" ")
        print("$" + line)

        if args [0] == "end":
            break
        elif args [0] == "show":
            print(budega)
        elif args [0] == "init":
            caixas = int(args[1])
            budega.__init__(caixas)
        elif args [0] == "arrive":
            pessoa = args[1]
            budega.arrive(pessoa)
        elif args [0] == "call":
            fila = int(args[1])
            budega.call(fila)
        elif args [0] == "finish":
            finalizar = int(args[1])
            budega.finish(finalizar)
        else:  
            print("fail: comando invalido")

main()