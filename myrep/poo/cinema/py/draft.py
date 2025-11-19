class Client:
    def __init__ (self, id: str, phone: int):
        self.__id = id
        self.__phone = phone

    def __str__ (self):
        return f"{self.__id}:{self.__phone} "
    
    def getId (self):
        return self.__id
    

class Theater:
    def __init__ (self, capacity: int):
        self
        self.seats: list [Client | None] = []
        for i in range (capacity):
            self.seats.append(None)
    
    def __str__ (self):
        assentos = "".join(["- " if x == None else str(x) for x in self.seats])
        return f"[{assentos.strip()}]"  

    def __search (self, name: str):
        for client in self.seats:
            if client != None and client.getId() == name:
                print("fail: cliente ja esta no cinema")
                return True
        return False
    
    def __verifyIndex (self, index: int):
        if index < 0 or index >= len(self.seats):
            print("fail: cadeira nao existe")
            return True
        return False

    def reserve(self, client: Client, index: int):
        if self.__verifyIndex(index):
            return True
        if self.seats[index] != None:
            print ("fail: cadeira ja esta ocupada")
            return
        self.__search(client.getId())
        self.seats[index] = client
    
    def cancel (self, name: str):
        for i, client in enumerate (self.seats):
            if client != None and client.getId() == name:
                self.seats[i] = None
                return
        print ("fail: cliente nao esta no cinema")

def main(): 
    cinema = Theater(0)

    while True:
        line = input()
        args: list [str] = line.split(" ")
        print("$" + line)

        if args [0] == "end":
            break
        elif args [0] == "show":
            print (cinema)
        elif args [0] == "init":
            capacity = int(args[1])
            cinema.__init__(capacity)
        elif args [0] == "reserve":
            id = args[1]
            phone = int(args[2])
            index = int(args[3])
            client = Client(id, phone)
            cinema.reserve(client, index)
        elif args [0] == "cancel":
            name = args[1]
            cinema.cancel(name)
        else:
            print("fail: comando invalido")

main()