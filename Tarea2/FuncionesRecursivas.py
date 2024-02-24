# Willy Estuardo Culajay Asturias
# Seccion A
# Carnet: 9490-22-3432

# Progrma interactivo que sirve para representar el uso de las funciones recursivas

#CONVERTIR NUMERO ENTERO DECIMAL A BINARIO.


def convertir_Binario(numero):
    
    if(numero == 0):
        return " "
    else:
        return convertir_Binario(numero//2)+str(numero%2)

# CONTAR DIGITOS

def Contar_Digitos(contar):
    if contar < 10:
        return 1
    else:
        return 1 + Contar_Digitos(contar//10)


#RAIZ CUADRA ENTERA

def Raiz_Cuadra_Entera(numero1):
    if numero1 < 0:
        raise ValueError("No se puede calcular raiz cuadrada de un numero negativo")
    def Calcular_Raiz_Cuadrada(aux):
        if aux * aux > numero1: 
            return aux -1
        else:
            return Calcular_Raiz_Cuadrada(aux+1)
    return Calcular_Raiz_Cuadrada(1)

#CONVERTIR UN NUMERO ROMANO A DECIMAL

def Convertir_a_Decimal(romano):
    romanos = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    def convertir_aux(romano):
        if not romano:
            return 0
        elif len(romano)==1:
            return romanos[romano[0]]
        else:
            if romanos[romano[0]] < romanos[romano[1]]:
                return romanos[romano[1]]-romanos[romano[0]] + convertir_aux(romano[2:])
            else:
                return romanos[romano[0]] + convertir_aux(romano[1:])
    return convertir_aux(romano)
    

#SUMA DE NUMEROS ENTEROS

def suma_numeros_enteros(numero2):
    if numero2 == 0:
        return 0
    else:
        return numero2 + suma_numeros_enteros(numero2-1)


try:   
    if __name__ == "__main__":
        opcion = 0
        while opcion != 6:
            print("\n***FUNCIONES RECURSIVAS****\n   \n1. CONVERTIR NUMERO DECIMAL A BINARIO.\n2. CONTAR DIGITOS DE UN NUMERO.\n"
            "3. OBTERNER RAIZ CUADRADA ENTERA.\n4. CONVERTIR NUMERO ROMANO A DECIMAL\n5. SUMA DE NUMEROS ENTEROS.\n6. SALIR \n")
            opcion = int(input("Ingrese la opcion a elegir: "))

            if opcion == 1:
                numero = int(input("\nIngrese un numero a convertir a Binario: "))
                print(convertir_Binario(numero))
                convertir_Binario(numero)
            elif opcion == 2:
                contar = int(input("\nIngrese un numero para determinar cuantos Digitos tiene: "))
                print(Contar_Digitos(contar))
                Contar_Digitos(contar)
            elif opcion == 3:
                numero1 = int(input("\nIngrese el numero a Calcular su Raiz: "))
                print("\nla raiz cuadrada de: ", numero1," es: ", Raiz_Cuadra_Entera(numero1))
                Raiz_Cuadra_Entera(numero1)
            elif opcion == 4:
                numero_romano = input("\nIngresa el numero romano a Convertir: ")
                print("En numero decimal es: ", Convertir_a_Decimal(numero_romano))
                Convertir_a_Decimal(numero_romano)
            elif opcion == 5:
                numero2 = int(input("\nIngrese el numero a sumar: "))
                print("El total es: ", suma_numeros_enteros(numero2))
                



except Exception as e:
    print(e)