"""
1) Faça uma função que receba três numeros inteiros: a,b e c, onde 'a' é maior que 1.
A função deve somar todos os inteiros entre b e c que sejam divisiveis por 'a' (inclusive b e c)
e retornar o resultado para a função principal.
"""
def somanumeros(a:int, b:int, c:int):
    soma = 0
    for i in range(b, c+1):
        if i % a == 0:
            soma = soma + i
    return soma

guardar = somanumeros(2,10,100)
print(guardar)
