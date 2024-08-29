"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.(ou qualquer outro time do campeonato atual)
"""

tabelaBrasileiro = ('Fortaleza','Botafogo', 'Palmeiras', 'Flamengo', 
                    'São Paulo', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 
                    'Atlético MG', 'Atlético PR', 'Internacional','Bragantino',
                    'Junventude', 'Grêmio','Criciúma','Fluminense',
                    'EC Vitória','Corinthians','Cuiabá', 'Atlético GO')

# exibe os 5 primeiros colocados
print('-'* 30)
print('{:^30}'.format('Tabela Brasileirão 2024'))
print('-'* 30)

print('{:^30}'.format('Os 5 primeiros colocados'))
print('='* 30)

for cont in range(len(tabelaBrasileiro[:5])):
    print(f'{cont + 1}º {tabelaBrasileiro[cont]}')

# exibe os 4 últimos colocados
print('='* 30)
print('{:^30}'.format('Os 4 últimos colocados'))
print('='* 30)

for c in range(0, len(tabelaBrasileiro[16:])):
    print(f'{c + 17}º {tabelaBrasileiro[c + 16]}')

# exibe em ordem alfabética
print('='* 30)
print('{:^30}'.format('Clubes em ordem alfabética'))
print('='* 30)

for cont in sorted(tabelaBrasileiro):
    print(cont)

"""
Como fiz o execicío em 2024 ao invés de usar o time Chapecoense, 
usei por padrão o time que estiver em oitavo lugar no campeonato

"""
# exibe o time que esta em 8º na tabela
print('='* 30)
print('{:^30}'.format('Time que esta em 8º na tabela'))
print('='* 30)
print(f'{tabelaBrasileiro[7]} esta na {tabelaBrasileiro.index(tabelaBrasileiro[7]) + 1}º posição do campeonato')

print('fim do programa')


