# 5)	Foi realizada uma pesquisa de algumas características físicas de cinco habitantes de uma certa região.
# De cada habitante foram coletados os seguintes dados:
#sexo, cor dos olhos (A – Azuis ou C – Castanhos), cor dos cabelos (L – Louros, P – Pretos ou C – Castanhos) e idade.

# a.	Faça uma função que leia esses dados em vetores.
# Determine, por meio de outra função, a média de idade das pessoas com olhos castanhos e cabelos pretos.
# Mostre esse resultado no programa principal.

# b.	Faça uma função que determine e devolva ao programa principal a maior idade entre os habitantes.

# c.	Faça uma função que determine e devolva ao programa principal a quantidade de
# indivíduos do sexo feminino cuja idade está entre 18 e 35 (inclusive) e que tenham olhos azuis e cabelos louros.

lista_sexo = [0] * 5
lista_olhos = [0] * 5
lista_cabelo = [0] * 5
lista_idade = [0] * 5

x = 1

def leitura_de_dados():
    x= 2
    for i in range(5):
        sexo = str(input('Digite o sexo | M ou F:\n'))
        lista_sexo[i] = sexo
    for j in range(5):
        olho = str(input('Digite a cor dos olhos:\n'
                      'A - Azuis\n'
                      'C - Castanhos\n'))
        lista_olhos[j] = olho
    for k in range(5):
        cabelo = str(input('Digite a cor dos cabelos:\n'
                      'L – Louros\n'
                      'P – Pretos\n'
                      'C – Castanhos\n'))
        lista_cabelo[k] = cabelo
    for l in range(5):
        idade = int(input('Digite a idade:\n'))
        lista_idade[l] = idade


def printalistas(list1: list, list2: list, list3: list, list4: list):
    print(list1)
    print(list2)
    print(list3)
    print(list4)


def media_olhos_castanhos_e_cabelo_preto(lista1: list, lista2: list, lista3: list):
    tot_oc_cp = 0
    tot_oc_cp_idades = 0
    for i in range(5):
        if lista_olhos[i] == 'C':
            if lista_cabelo[i] == 'P':
                tot_oc_cp += 1
                tot_oc_cp_idades += lista_idade[i]
    print(f'A média de idades de pessoas com olhos castanhos e cabelo preto é {(tot_oc_cp_idades / tot_oc_cp)}\n'
          f'Nº de Pessoas: {tot_oc_cp} | Total Idades: {tot_oc_cp_idades}')


def maior_idade_entre_os_habitantes():
    tot_idades = 0
    for i in range(5):
        tot_idades += lista_idade[i]
    media_idades = tot_idades / 5
    print(f'A média de idades dos 5 habitantes é: {media_idades}')


def muie_entre_18a35_oa_cl():
    tot_idades = 0
    tot_muie = 0
    for i in range(5):
        if lista_sexo[i] == 'F':
            if lista_cabelo[i] == 'L' and lista_olhos[i] == 'A':
                if lista_idade[i] >= 18 and lista_idade[i] <= 35:
                    tot_idades += lista_idade[i]
                    tot_muie += 1
    print(f'A média de idade das mulheres com cabelo loiro e olho azul é: {tot_idades / tot_muie}')

# ====================== Chamando as funções

leitura_de_dados()
printalistas(lista_idade,lista_cabelo, lista_olhos, lista_sexo)
media_olhos_castanhos_e_cabelo_preto(lista_olhos, lista_cabelo, lista_idade)
maior_idade_entre_os_habitantes(lista_idade)
muie_entre_18a35_oa_cl()
