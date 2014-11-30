
class Ferias(object):

	def __init__(self, sal_bruto ):
		self.sal_bruto = sal_bruto
		#self.salDia = self.ultimo_salario / 30

	def CalculoFerias(self):
		#Calcular o numero de dias entre as datas
		self.umterco = self.sal_bruto / 3
		self.proventos = self.sal_bruto + self.umterco
		return self.proventos, self.umterco

	def CalculoInss(self):
		if self.proventos <= 1317.07:
			self.vrinss = 0.08 * self.proventos
			self.indiceinss = "8%"
		elif self.proventos <= 2195.12:
			self.vrinss = 0.09 * self.proventos
			self.indiceinss = "9%"
		elif self.proventos <= 4390.24:
			self.vrinss = 0.11 * self.proventos
			self.indiceinss = "11%"
		else:
			self.vrinss = 0.11 * 4390.24
			self.indiceinss = "11%"
		return self.vrinss, self.indiceinss

	def ImprimeDadosFerias(self):
		self.rferias = self.CalculoFerias()
		self.rInss = self.CalculoInss()
		self.proventos = self.rferias[0]
		self.descontos = self.rInss[0]
		self.vrliquidoferias = self.proventos - self.descontos