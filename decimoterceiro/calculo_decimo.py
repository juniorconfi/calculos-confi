
from datetime import date

class DecimoTerceiro(object):

	def __init__(self, data_admissao, sal_bruto ):
		self.data_admissao = data_admissao
		self.sal_bruto = sal_bruto
		#self.salDia = self.ultimo_salario / 30

	def CalculoDecimoTerceiro(self):
		#Pegar o Mes da data de saida
		self.mes_admissao = int(self.data_admissao.strftime("%m"))
		self.dia_admissao = int(self.data_admissao.strftime("%d"))
		#Calcular 1/12 do Salario
		self.UmDozeAvos = self.sal_bruto / 12
		# Calcular o Decimo Terceiro proporcional
		#Condicao - se o dia da data da saida for menor que 14 dias
		#e subtraido 1 mes 
		if self.dia_admissao > 16 :
			self.avos_decimo = (12 - self.mes_admissao)
		else:
			self.avos_decimo = (13 - self.mes_admissao) 
					
		self.dterceiro = self.avos_decimo * self.UmDozeAvos
		
		return self.dterceiro, self.avos_decimo
		#print(" %d/12 avos , valor: R$ %f" % (self.mes, self.dterceiro) )

	def CalculoInssDecimo(self):
		if self.dterceiro <= 1317.07:
			self.vrInssDecimo = 0.08 * self.dterceiro
			self.indiceInssDecimo = "8%"
		elif self.dterceiro <= 2195.12:
			self.vrInssDecimo = 0.09 * self.dterceiro
			self.indiceInssDecimo = "9%"
		elif self.dterceiro <= 4390.24:
			self.vrInssDecimo = 0.11 * self.dterceiro
			self.indiceInssDecimo = "11%"
		else:
			self.vrInssDecimo = 0.11 * 4390.24
			self.indiceInssDecimo = "11%"
		return self.vrInssDecimo, self.indiceInssDecimo

	def ImprimeDadosDecimo(self):
		self.rdecimoterceiro = self.CalculoDecimoTerceiro()
		self.rinssdecimo = self.CalculoInssDecimo()
		self.proventos = self.rdecimoterceiro[0] 
		self.descontos = self.rinssdecimo[0]
		self.vrdecimoliquido = self.proventos - self.descontos