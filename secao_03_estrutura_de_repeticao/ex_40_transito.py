"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil carros.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil carros.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.
"""

from statistics import mean

def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""
    acidentes = []
    carros = []
    cidade_pequena = []
    nomes_cidades = []
    indices_acidentes = []
    for nome, carro, acidente in cidades:
        nomes_cidades.append(nome)
        carros.append(carro)
        acidentes.append(acidente)
        indice = acidente/carro
        indices_acidentes.append(indice)
        if carro <= 150_000:
            cidade_pequena.append(acidente)

    maior_indice = max(indices_acidentes)
    nome_maior_indice = nomes_cidades[indices_acidentes.index(maior_indice)]
    menor_indice = min(indices_acidentes)
    nome_menor_indice = nomes_cidades[indices_acidentes.index(menor_indice)]
    maior_indice*=1000
    menor_indice*=1000
    media_carros = mean(carros)
    media_acidentes = mean(cidade_pequena)

    print(f'O maior índice de acidentes é de {nome_maior_indice}, com {maior_indice:.1f} acidentes por mil carros.')
    print(f'O menor índice de acidentes é de {nome_menor_indice}, com {menor_indice:.1f} acidentes por mil carros.')
    print(f'O média de veículos por cidade é de {media_carros}.')
    print(f'A média de acidentes total nas cidades com menos de 150 mil carros é de {media_acidentes:.1f} acidentes.')