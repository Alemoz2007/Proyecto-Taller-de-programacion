def main():
    #Falta el mensaje de bienvenida y la descripción.
    print("Por favor escoga alguno de los siguientes números, \
dependiendo del método de cifrado que desea utilizar")
    continuar = True
    while continuar:
        try:
             indicación=int(input("Diguite '1' para el método de cifrado césar; '2' para \
el cifrado monoalfabético con palabra clave; '3' para el cifrado vigenère; '4' para el \
el cifrado PlayFair; '5' para el cifrado Rail Fence; '6' para el cifrado escítala:  "))
             while indicación not in (1, 2, 3, 4, 5, 6):
                 indicación = int(input("Digite algún número válido para continuar: ")) #indicación es solo para seleccionar método
             limpiar_pantalla() #Simplemente da orden
             if indicación == 1: #Cifrado César
                 print("Cifrado César")
                 selección = int(input("Digite '1' si lo que desea es codificar, de lo contrario, digite '2' para decodificar: "))
                 while selección not in (1, 2):
                     selección=int(input("Digite uno de los valores válidos: "))
                 if selección == 1: #codifica Cesar
                     print("Codificar") # Acá iría cesarCod(texto, desplazamiento),  
                 else: #decodifica Cesar
                     print("Decodificar") # Acá iría cesarDec(texto, desplazamiento)
             elif indicación == 2: #Cifrado Monoalfabético con Palabra Clave
                 print("Cifrado Monoalfabético con Palabra Clave")
                 selección = int(input("Digite '1' si lo que desea es codificar, de lo contrario, digite '2' para decodificar: "))
                 while selección not in (1, 2):
                     selección=int(input("Digite uno de los valores válidos: "))
                 if selección == 1: #codifica monoalfabetico
                     print("Codificar") # Acá iría monoCod(texto, palabra)
                 else: #decodifica monoalfabetico
                     print("Decodificar") # Acá iría monoDec(texto, palabra)
             elif indicación == 3: #Cifrado Vigenère
                 print("Cifrado Vigenère")
                 selección = int(input("Digite '1' si lo que desea es codificar, de lo contrario, digite '2' para decodificar: "))
                 while selección not in (1, 2):
                     selección=int(input("Digite uno de los valores válidos: "))
                 if selección == 1: #codifica Vigenère
                     print("Codificar") # Acá iría vigenereCod(texto, palabra)
                 else:  #decodifica Vigenère
                     print("Decodificar") # Acá iría vigenerDec(texto, palabra)
             elif indicación == 4:#Cifrado PlayFair
                 print("Cifrado PlayFair") 
                 selección = int(input("Digite '1' si lo que desea es codificar, de lo contrario, digite '2' para decodificar: "))
                 while selección not in (1, 2):
                     selección=int(input("Digite uno de los valores válidos: "))
                 if selección == 1:  #codifica PlayFair
                     print("Codificar") # Acá iría playfairCod(texto, palabra)
                 else: #decodifica PlayFair
                     print("Decodificar") # Acá iría playfairDec(texto, palabra)
             elif indicación == 5:
                 print("Cifrado Rail Fence") #Rail Fence
                 selección = int(input("Digite '1' si lo que desea es codificar, de lo contrario, digite '2' para decodificar: "))
                 while selección not in (1, 2):
                     selección=int(input("Digite uno de los valores válidos: "))
                 if selección == 1: #Codifica Rail Fence
                     texto=input("Diguite el texto que desea codificar por favor escriba el texto dentro de dobles comillas: ")
                     railfenceCod(texto)
                 else: #Decodifica Rail Fence
                     texto=input("Diguite el texto que desea decodificar, por favor escriba el texto dentro de dobles comillas: ")
                     railfenceDec(texto)
             else:  #Escítala
                 print("Cifrado Escítala")
                 selección = int(input("Digite '1' si lo que desea es codificar, de lo contrario, digite '2' para decodificar: "))
                 while selección not in (1, 2):
                     selección=int(input("Digite uno de los valores válidos: "))
                 if selección == 1: #Codifica  Escítala
                     texto=input("Diguite el texto que desea codificar, por favor escriba el texto dentro de dobles comillas: ")
                     líneas=input("Diguite la cantidad de vueltas que desea utilizar: ")
                     escitalaCod(texto, líneas)
                 else: #Decodifica  Escítala
                     texto=input("Diguite el texto que desea decodificar, por favor escriba el texto dentro de dobles comillas: ")
                     líneas=input("Diguite la cantidad de vueltas que utilizó: ")
                     escitalaDec(texto, líneas)
        except Exception as e:
            print(f"Error:{e}")
            continuar = False
            continuar = repetir() 

def limpiar_pantalla():
    """Función que se encarga de imprimir líneas en blanco para 'limpiar' la pantalla
No tiene entradas ni restricciones, solo imprime 40 líneas en blanco"""
    print("\n" * 10)
def repetir():
    """Función booleana que se encarga de preguntarle al usuario sí desea volver a utilizar el programa o no, además, en el caso de que la respuesta sea
negativa, se encarga de imprimir el mensaje de despedida.
Entradas: No tiene.
Restricciones: El usuario solo puede escribir 's' o 'n', además de que la salida es un valor booleano.
Salidas: True en el caso de que el usuario desee continuar, en caso contrario False, después de mostrar el mensaje de  despedida."""
    print()
    print("¿Desea volver a utilizar el programa?")
    respuesta=input("Digite 'S' en caso de que desea utilizarlo de nuevo, de lo contrario digite 'N': ")
    respuesta = respuesta.lower()
    while respuesta not in ["s","n"]:
        respuesta = input("¿Desea utiliza el programa de nuevo? Digite 'S' o 'N': ")
        respuesta = respuesta.lower()
    if respuesta == "s":
        return True
    else:
        print("Le agradecemos por utilizar el programa. Hasta luego")
        return False
    

main()
   
    
    
