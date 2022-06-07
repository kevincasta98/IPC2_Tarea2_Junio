from Nodo import Nodo


class ListaCircularDobleEnlazada():
    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None 
        self.Size = 0
    
    def insertarNumeroAlFinal(self,num):
        nuevoNumero = Nodo(num)
        self.Size+=1
        if self.primero == None:
            self.primero = self.ultimo = nuevoNumero
        else:
            self.ultimo.siguiente = nuevoNumero
            nuevoNumero.Anterior = self.ultimo
            self.ultimo = nuevoNumero


        self.ultimo.siguiente = self.primero
        self.primero.Anterior = self.ultimo

    def imprimir(self):
        print("Elementos de la lista circular")
        aux=self.primero
        while(aux!=None):
            print("Digito:",aux.numero)
            if (aux.siguiente==self.primero):
                return
            aux=aux.siguiente

    def buscar(self, valor_buscado):
        aux:Nodo=self.primero
        while(aux!=None):
            if (aux.numero==valor_buscado):
                print("Digito anterior:", aux.Anterior.numero)
                print("Digito actual:",aux.numero)
                print("Digito siguiente",aux.siguiente.numero)

            if (aux.siguiente==self.primero):
                return
            aux = aux.siguiente

prueba = ListaCircularDobleEnlazada()
print("=============== Llenado de lista Circular ===============")
prueba.insertarNumeroAlFinal(1)
prueba.insertarNumeroAlFinal(2)
prueba.insertarNumeroAlFinal(3)
prueba.insertarNumeroAlFinal(4)
prueba.insertarNumeroAlFinal(5)
prueba.insertarNumeroAlFinal(6)
prueba.insertarNumeroAlFinal(7)
prueba.imprimir()
print("\n=============== Metodo de Busqueda ===============")
buscado = int(input("Seleccione el numero a buscar en la lista: "))
prueba.buscar(buscado)
