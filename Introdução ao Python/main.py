times = ['Chelsea', 'Palmeiras', 'Al Ahly', 'Al Hilal', 'Monterrey']

print(times[:3], '\n')

print(times[3:], '\n')

print(sorted(times), '\n')

# Como o Barcelona não esta na lista, vou pesquisar o Al Hilal
print(times.index('Al Hilal'), '\n')

print('# ------------------------------------------------------------------- #', '\n')

loja1 = {'Samsung s20', 'Samsung s21', 'Samsung A51'}

loja2 = {'Xiaomi Redmi 10', 'Poco X3'}

print('Opcoes = ', loja1 | loja2, '\n')

print('Loja1 = ', loja1, '\n')
print('Loja2 = ', loja2, '\n')

print('# ------------------------------------------------------------------- #', '\n')

nome = input('Nome do aluno: ')
media = input('Media do aluno: ')

if int(media) >= 60:
    situacao = 'AP'
elif int(media) < 30:
    situacao = 'RP'
else:
    situacao = 'NP3'

aluno = {'nome': nome, 'media': media, 'situacao': situacao}

print(aluno)
