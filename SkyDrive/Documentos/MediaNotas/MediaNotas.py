from statistics import mean

class MediaNotas:

	__notas = []
	__nome 

	def __init__(self, nome, notas = []):
		self.__nome = nome
		self.__notas = notas

	def nome_aluno(self, nome):
		return self.nome

	def calcular_media(self):
		media = mean(self.notas)	
		return media




