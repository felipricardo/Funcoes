"""
4)	Faça uma função que receba cinco valores inteiros, e retorne o maior valor. Faça uma segunda função que receba 
também cinco valores e retorne o menor deles.
"""

def encontraMaior(*numeros):
    omaior = 0
    for i in numeros:
        if i > omaior:
            omaior = i
    return omaior

guardar_resultado = encontraMaior(1)
print("guardar_resultado", guardar_resultado)
guardar_resultado = encontraMaior(1,2,3,4,5)
print("guardar_resultado", guardar_resultado)
