"""
Exercício 04 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

    >>> vogal_ou_consoante("F")
    'consoante'
    >>> vogal_ou_consoante("a")
    'vogal'
    >>> vogal_ou_consoante('c')
    'consoante'
    >>> vogal_ou_consoante('U')
    'vogal'
"""


from http.client import LENGTH_REQUIRED


def vogal_ou_consoante(letra):
    """Escreva aqui em baixo a sua solução"""
    letra = letra.lower()
    if letra =="a":
     print("'vogal'")
    elif letra == "e":
     print("'vogal'")
    elif letra == "i":
     print("'vogal'")
    elif letra == "o":
     print("'vogal'")
    elif letra == "u":
     print("'vogal'")
    else:
     print("'consoante'")
