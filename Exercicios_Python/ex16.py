'''
Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. 
Depois imprima a soma dos valores.

A string deve ter valor  "1,3,4,6,10,76"
'''

def soma(string):
    numeros = string.split(',')
    soma = sum(map(int, numeros))
    return soma

string = "1,3,4,6,10,76"
soma = soma(string)
print(soma)
