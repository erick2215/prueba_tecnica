import os
os.system('cls')

def diccionario(frase):
    conteo={}
    llaves=conteo.keys()
    for i in frase:
        if i  in llaves:
            conteo[i]+=1
        else:
            conteo[i]=1
                   
    return conteo        

print(diccionario('Mississippi'))
print(diccionario('python! is better'))