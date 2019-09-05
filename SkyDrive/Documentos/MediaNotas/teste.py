from MediaNotas import MediaNotas

#importando a biblioteca para calcular a media das notas em um array
#biblioteca de deṕuração

import pdb 
pdb.set_trace()

nome_aluno = str(input('Informe seu nome: '))

notas = []

for x in range(0,4):
	nota = float(input('Informe a nota: '))
	notas.append(nota)

media_notas = MediaNotas(nome_aluno, notas)
# o mean calcula media de um array
media = media_notas.calcular_media()

if media >= 7:
	print("Sua media é: ", media, "e você foi aprovado!")

elif media < 7 and media >= 4:
	print(nome_aluno,"Sua media é: ", media, "e você está em exame")
else:
	print(nome_aluno,"Sua media é: ", media, "e você está ")




