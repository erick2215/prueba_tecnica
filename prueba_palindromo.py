#Importamos la libreria "os".
import os 
#utilizamos el comando 'os.system('cls')' para limpiar pantalla y mostrar solo el resultado.
os.system('cls')

#definimos la función 'palin' y como parametro utilizamos'palabra'.
def palin (palabra):
    palabra= palabra.lower().replace(' ','').replace(',','').replace('.','')
    return palabra== palabra[::-1]
        
print(palin("race car"))
print(palin("not a palindrome"))
print(palin("A man, a plan, a canal. Panama"))
print(palin("never odd or even"))
print(palin("nope"))
print(palin("almostomla"))