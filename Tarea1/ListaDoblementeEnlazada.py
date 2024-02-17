import os
from graphviz import Digraph

class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    
    def ingresar_alPrincipio(self,nombre,apellido,carnet):
        nodon = Nodo(nombre, apellido, carnet)
        if not self.primero:
            self.primero = nodon
            self.ultimo = nodon
        else:
            nodon.siguiente = self.primero
            self.primero.anterior = nodon
            self.primero = nodon
          

    def ingresar_alUltimo(self, nombre, apellido, carnet):
        nodon = Nodo(nombre, apellido, carnet)
        if not self.ultimo:
            self.primero = nodon
            self.ultimo = nodon
        else:
            nodon.anterior = self.ultimo
            self.ultimo.siguiente = nodon
            self.ultimo = nodon

    def eliminar_por_Valor(self,dato):
        actual = self.primero
        while actual:
            if actual.nombre == dato or actual.apellido == dato or actual.carnet == dato:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.primero = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.ultimo = actual.anterior
                return
            actual = actual.siguiente

            

    def mostrar_listad(self):
        recorrer = self.primero
        print("None", end="<- ")
        while recorrer:
            print(f"{"Nombre: "}{recorrer.nombre}{" Apellido: "}{recorrer.apellido}{" Carnet: "}{recorrer.carnet}", end =" <-> ")
            recorrer = recorrer.siguiente  
        print("None")

def generar_grafico(lista):
    os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin'
    dot = Digraph()
    recorrer = lista.primero

    while recorrer:
        dot.node(f"{recorrer.nombre}_{recorrer.apellido}", label = f"{recorrer.nombre} {recorrer.apellido}\n({recorrer.carnet})")
        if recorrer.siguiente:
            dot.edge(f"{recorrer.nombre}_{recorrer.apellido}", f"{recorrer.siguiente.nombre}_{recorrer.siguiente.apellido}", dir = 'both')
        if recorrer.anterior:
            dot.edge(f"{recorrer.nombre}_{recorrer.apellido}", f"{recorrer.anterior.nombre}_{recorrer.anterior.apellido}", dir = 'both')
        recorrer = recorrer.siguiente
    dot.graph_attr['rankdir'] = 'LR'
    dot.render("lista_doblemente_enlazada", format = 'png', cleanup = True)


try:    
    if __name__ == "__main__":
        opcion = 0
        lista = ListaDobleEnlazada()
        while opcion != 6:
            print("\n--- Lista Doblemente Enlazada ---\n 1. Agregar al Principio\n 2. Agregar al Final\n 3. Eliminar por Valor\n 4. Mostrar Lista\n 5. Generar Grafico\n 6. Salir\n")
            opcion = int(input("Ingrese su opción "))

            if opcion == 1:
                nombre = input("Ingrese Nombre: ")
                apellido = input("Ingrese Apellido: ")
                carnet = input("Ingrese Carnet: ")
                lista.ingresar_alPrincipio(nombre, apellido, carnet)

            elif opcion == 2:
                nombre = input("Ingrese Nombre: ")
                apellido = input("Ingrese Apellido: ")
                carnet = input("Ingrese Carnet: ")
                lista.ingresar_alUltimo(nombre, apellido, carnet)

            elif opcion == 3:
                dato = input("Ingrese Dato a Eliminar: ")
                lista.eliminar_por_Valor(dato)
                print("..... Informacion...Eliminada....")
            
            elif opcion == 4:
                lista.mostrar_listad()

            elif opcion == 5:
                generar_grafico(lista)
                print("Representacion Grafica de la lista Doblemente enlazda Generada con Exito")
            elif opcion == 6:
                break
            else:
                print("Opcion ingresada no valida, vuelve a intentarlo")


except Exception as e:
    print(e)







        

        
