import graphviz # importamos la libreria de graphviz para generar un diagrama de arbol para representar el arbol que vamos a crear

class Nodo: # creamos la clase nodo para poder crear los nodos
    def __init__(self, valor): # mandamos el valor que vamos a incertar en el nodo
        self.valor = valor
        self.izquierda = None # indica que el lado izquierdo no hay ningun valor // nodo hoja
        self.derecha = None # indica que del lado derecho no hay ningun valor

class Arbol_ABB: # creamos la clase arbol para generar las funciones de Insertar, Buscar, y Borrar nodos

    def __init__(self): # creamos el constructor de el nodo raiz, es el nodo mas importante ya que despues se agregan los demas nodos
        self.raiz = None # al inicialiar la raiz no tiene ningun valor del lado izquierdo ni del lado derecho
    
    def insertar(self, valor): #creamos la primer funcion de insertar
        self.raiz = self.insertar_Nodo(valor, self.raiz)# creamos otra funcion de recursividad que nos ayudara a ir insertando los datos (nodos en el arbol)
    
    def insertar_Nodo(self, valor, nodo): #creamos la funcion recursiva de insertar nodo
        if nodo == None: # si no hay nodos en el arbol lo inicializa ingresando la raiz principal, o si ya hay raiz, inserta el nodo ya sea del lado derecho o lado izquierdo
            return Nodo(valor)
        if valor < nodo.valor: # aqui valida si el valor a insertar es menor al valor que se encuentra en el nodo, si es menor lo manda al lado izquierdo
            nodo.izquierda = self.insertar_Nodo(valor, nodo.izquierda) # si no hay valor lo agrega al lado izquierdo del nodo, si hay valor vuele a realizar la funcion recursiva y manda el valor y el nodo izquierdo como parametros 
        if valor > nodo.valor: # aqui valida si el valor a insertar es mayor al valor que se encuentra en el nodo, si es mayor lo mandal al lado derecho 
            nodo.derecha = self.insertar_Nodo(valor, nodo.derecha) # si no hay valor lo agrega al lado derecho del nodo, si hay valor vuelve a realizar al funcion recursiva y manda el valor con el nodo.derecho como parametro                                  
        return nodo
    
    def buscar(self,valor):# creamos la funcion de buscar dentro del arbol
        return self.buscar_arbol(self.raiz,valor) #creamos otra funcion de recursividad que nos ayudara a buscar el valor solocitado dentro del arbol
    
    def buscar_arbol(self, nodo, valor): #creamos la funcion recursiva de buscar nodo
        if nodo == None: # si el valor es igual a nada devulve el mensaje, valor no encontrado
            print("No se encontro el valor buscado...")
           
        elif nodo.valor == valor: #si el valor buscado es la raiz principal devulvel el valor encontrado,
            print("Valor encontrado")
            return valor
        elif valor < nodo.valor: # si el valor buscado es menor a la raiz dada se va por la izquierda
            return self.buscar_arbol(nodo.izquierda, valor)# retornamos de nuevo la funcion de buscar enviando a la izquierda
        else:
            return self.buscar_arbol(nodo.derecha, valor)# si el valor buscado es mayor a la raiz dada se va por la derecha
        return nodo
    
    def eliminar(self,valor):#creamos la clase eliminar, en la cual toma un valor, el cual es el valor que se desea eliminar del arbol
        self.raiz = self.eliminar_nodo(self.raiz,valor)#llama al metodo recursivo eliminar_nodo con la raiz del arbol y el valor a eliminar, el resultado de esta llamada asigna de nuevo 
        return print("Numero Eliminado correctamente")#a self.raiz. lo que actualiza la raiz del arbol si es necesario despues de la eliminacion
    
    def eliminar_nodo(self,nodo,valor):# funcion recursiva para ubicar el valor en el arbol a eliminar que toma dos parametros, el nodo actual del arbol y el valor que se desea elminiar
        if not nodo:# si el nodo actual es Nulo o no tiene valor no hace nada simplemente devuelve el nodo actual
            print("nodo a eliminar no existe dentro del arbol")
            return nodo
        if valor < nodo.valor:# si el valor a eliminar es menor al valor del nodo actual se va por la izquierda  
            nodo.izquierda = self.eliminar_nodo(nodo.izquierda, valor)#se llama de nuevo el metodo recursivo y envia como parametros el hijo izquierdo del nodo actual
        elif valor > nodo.valor:# si el valor a eliminar es mayor al valor del nodo actual se va por la derecha
            nodo.derecha = self.eliminar_nodo(nodo.derecha, valor)#se llama de nuevo el metodo recursivo y envia como parametro el hijos derecho del nodo actual
        else:
            if not nodo.izquierda:#comprueba si el nodo actual no tiene hijo izquierdo
                return nodo.derecha#si no tiene hijo izquierdo, devuelve el hijo derecho del nodo actual 
            if not nodo.derecha:#comprueba si el nodo actual no tiene hijo derecho
                return nodo.izquierda# si no tiene hijo derecho, devuelve el hijo izquierdo del nodo actual
            aux = self.encontrar_valor_minimo(nodo.derecha)# se crea una variable temporal aux que toma el valor de una funcion que sirve para encontrar el valor minimo del subarbol derecho
            nodo.valor = aux.valor#se remplaza el valor del nodo actual con el valor del nodo minimo encontrado      
            nodo.derecha = self.eliminar_nodo(nodo.derecha,aux.valor)#llama recursivamente a la funcion para eliminar el nodo mininmo el sub arbol derecho
        return nodo # retorna el nodo actual
    
    def encontrar_valor_minimo(self,nodo):# se crea una funcion para encontrar el valor minimo en el subarbol derecho
        while nodo.izquierda:#mientras el nodo actual tenga un hijo izquierdo, continua su busqueda hacia la izquierda del subarbol
            nodo = nodo.izquierda#avanza hacia el hijo izquierdo del nodo actual
        return nodo#retorna el nodo actual una vez que se alcanza un nodo que no tiene hijo izquierdo. lo que indica que este es el nodo nimimo en el subarbol
    
    def cargar_datos_txt(self, nombre_archivo):# funcion de cargar archivos 
        valores = []# se crea una lista para almacenar los valores del archivo recibido
        with open(nombre_archivo, 'r') as archivo:# se abre el archivo en modo de lectura
            for linea in archivo:# leemos linea por linea del archivo
                valores.append(int(linea.strip()))# se convierte cada linea a entero y la agregamos a la lista de valores
            self.construir_arbol(valores)# se hace llamada de la funcion para crear el arbol binario a partir de los valores dados

    def construir_arbol(self, valores):# creamos la funcion para construir el arbol binario
        if not valores:# si la lista enviada no contine informacion retornamos un mensaje
            return print("no hay valores dentro del archivo")
        valores.sort() # se ordenan los valores de la lista
        self.raiz = self.construir_aux(valores) #hace el llamado a la funcion aux recursiva para construir el arbol

    def construir_aux(self, valores):# funcion aux para construir el arbol binario
        if not valores:# si la lista enviada no contiene informacion retornamos None
            return None
        medio = len(valores)//2# se encuentra el indice medio de la lista 
        nodo = Nodo(valores[medio])# se crea un nodo con el valor medio de la lista
        nodo.izquierda = self.construir_aux(valores[:medio])#se llama de nuevo la funcion para construir el subarbol izquierdo
        nodo.derecha = self.construir_aux(valores[medio+1:])# se llama de nuevo la funcion para construir el subarbol derecho
        return nodo      
        

    def generar_graphviz(self): # la funcion se encarga de generar la representacion del arbol en Graphviz 
        dot = graphviz.Digraph() # se crea un objeto Digraph de Graphviz llamado dot representa un objeto dirigido 
        self.generar_graphivz_Arbol(self.raiz, dot) # llama la funcion Generar graphviz recibe como parametro la raiz del arbol y el objeto dot
        return dot # devuelve el objeto que contine la representacion del arbol en formato Graphviz
    
    def generar_graphivz_Arbol(self, nodo, dot): #funcion auxiliar para construir el Graphviz que recibe como parametros el nodo actual del arbol y dot que es el objeto
        if nodo is not None: # verifica si el valor que estamos enviando es vacio, si es vacio para la recursion.
            dot.node(str(nodo.valor)) # si tiene valor, agrega el nodo al objeto dot con el valor del nodo actual, se convierte el valor a cadena str ya que graphviz requiere que las etiquetas sean cadenas
            if nodo.izquierda is not None:# verifica si el nodo enviado tenien un hijo del lado izquiero 
                dot.edge(str(nodo.valor), str(nodo.izquierda.valor)) # crea un enlace (arista) desde el nodo actual al nodo hijo del lado izquierdo estro representa la relacion de padre he hijo
                self.generar_graphivz_Arbol(nodo.izquierda, dot) # vuelve a llamar la funcion recursiva con el nodo hijo izquierdo como nuevo nodo actual 
            if nodo.derecha is not None: # verifica si el valor que estamos enviando es vacio, si es vacio para la recursion
                dot.edge(str(nodo.valor), str(nodo.derecha.valor)) # crea un enlace (arista ) desde el nodo actual al nodo hijo del lado derecho
                self.generar_graphivz_Arbol(nodo.derecha, dot) # vuelve a llamar la funcion recursiva con el nodo hijo derecho como nuevo nodo actual

def menu():
    arbol = Arbol_ABB()
    while True:
        print("\nMenu del Programa")
        print("\n1. Insertar Datos en el Arbol")
        print("\n2. Buscar Datos en el Arbol")
        print("\n3. Eliminar Dato en el Arbol")
        print("\n4. Cargar Datos desde Archivo txt")
        print("\n5. Generar Representacion del Arbol")
        print("\n6. Salir")

        opcion = input("\nSeleccione la opcion que desea realizar: ")

        if opcion == '1':
            valor = int(input("\nIngrese el numero a Insertar: "))
            arbol.insertar(valor)
            print("Numero Ingresado Correctamente")
        
        elif opcion == '2':
            valor = int(input("\nIngrese el numero a Buscar: "))
            arbol.buscar(valor)

        elif opcion == '3':
            valor = int(input("\nIngrese el numero a Eliminar: "))
            arbol.eliminar(valor)
            #print("Numero Eliminado correctamente")
        
        elif opcion == '4':
            nombre = input("\nIngrese el Nombre del archivo: ")
            arbol.cargar_datos_txt(nombre)
            print("Informacion cargada correctamente")
        
        elif opcion == '5':
            dot = arbol.generar_graphviz()
            dot.render('arbol_binario', format='png', cleanup= True)
            print("\nRepresentacion Grafica creada con Exito")

        elif opcion == '6':
            break
        else:
            print("opcion no valida, Intente de nuevo")

if __name__ == "__main__":
    menu()








        

