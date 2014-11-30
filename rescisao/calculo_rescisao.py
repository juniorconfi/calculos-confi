
from datetime import date

class Rescisao(object):

	def __init__(self, data_admissao, data_saida, ultimo_salario ):
		self.data_admissao = data_admissao
		self.data_saida = data_saida
		self.ultimo_salario = ultimo_salario
		#self.salDia = self.ultimo_salario / 30

	def CalculoSaldoSalario(self):
		#Calcular o numero de dias entre as datas
		self.primDiaMes = date(self.data_saida.year, self.data_saida.month, 1)
		self.difdatas = self.data_saida - self.primDiaMes
		self.saldo_dias = self.difdatas.days + 1
		self.salDia = self.ultimo_salario / 30
		self.saldo_salario = self.salDia * self.saldo_dias 
		return self.saldo_salario , self.saldo_dias

	def CalculoInssSaldo(self):
		if self.saldo_salario <= 1317.07:
			self.vrInssSaldo = 0.08 * self.saldo_salario
			self.indiceInssSaldo = "8%"
		elif self.saldo_salario <= 2195.12:
			self.vrInssSaldo = 0.09 * self.saldo_salario
			self.indiceInssSaldo = "9%"
		elif self.saldo_salario <= 4390.24:
			self.vrInssSaldo = 0.11 * self.saldo_salario
			self.indiceInssSaldo = "11%"
		else:
			self.vrInssSaldo = 0.11 * 4390.24
			self.indiceInssSaldo = "11%"
		return self.vrInssSaldo, self.indiceInssSaldo

	def CalculoDecimoTerceiro(self):
		#Pegar o Mes da data de saida
		self.mes_saida = int(self.data_saida.strftime("%m"))
		self.mes_admissao = int(self.data_admissao.strftime("%m"))
		self.dia_admissao = int(self.data_admissao.strftime("%d"))
		self.dia_saida = int(self.data_saida.strftime("%d"))
		#Calcular 1/12 do Salario
		self.UmDozeAvos = self.ultimo_salario / 12
		# Calcular o Decimo Terceiro proporcional
		#Condicao - se o dia da data da saida for menor que 14 dias
		#e subtraido 1 mes 
		if self.dia_admissao > 15 and self.dia_saida < 15:
			self.avos_decimo = (self.mes_saida - self.mes_admissao) - 1
		
		elif self.dia_admissao > 15 or self.dia_saida < 15:
			self.avos_decimo = (self.mes_saida - self.mes_admissao) 

		else:
			self.avos_decimo = (self.mes_saida - self.mes_admissao) + 1
					
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

	def CalculoFerias(self): # Esse sistema de calculo nao funciona!!!!
		#Pegar o mês da data de saida
		self.mesSai = int(self.data_saida.strftime("%m"))
		#Pegar o mes da data de admissao para calcular o periodo de ferias
		self.mesEnt = int(self.data_admissao.strftime("%m"))
		#Calculo do valor de um 1/12 avos
		self.UmDozeAvos = self.ultimo_salario / 12
		#Calcular o avos de ferias
		self.avosFerias = self.mesSai - self.mesEnt
		#Pegar a quantidade dos dias entre a data da saida e o do mes anterior
		#se for menor que 15 dias perde 1/12
		self.mesAnterior = date(self.data_saida.year, self.data_saida.month - 1, self.data_admissao.day)
		self.difdatasFerias = self.data_saida - self.mesAnterior
		if self.difdatasFerias.days < 15:
			self.avosFerias -= 1
		else:
			pass
		self.feriasproporcionais = self.avosFerias * self.UmDozeAvos
		return self.feriasproporcionais, self.avosFerias

		
	def ImprimeDadosRescisao(self):
		self.rSaldo = self.CalculoSaldoSalario()
		self.rInssSaldo = self.CalculoInssSaldo()
		self.rDecimoTerceiro = self.CalculoDecimoTerceiro()
		self.rInssDecimo = self.CalculoInssDecimo()
		self.rFerias = self.CalculoFerias()
		self.proventos = self.rSaldo[0] + self.rDecimoTerceiro[0] + self.rFerias[0]
		self.descontos = self.rInssSaldo[0] + self.rInssDecimo[0]
		self.vrRescisaoLiquido = self.proventos - self.descontos
		#return self.rSaldo, self.rDecimoTerceiro, self.rFerias





#dtadm = date(2014,8,16)
#dtsaid = date(2014,11,14)
#ultsal = 2300
#r1 = Rescisao(dtadm, dtsaid, ultsal)
#print(r1.CalculoSaldoSalario())
#print(r1.data_saida.toordinal())
#r1.CalculoSaldoSalario()
#print(r1.saldo_salario)
#print(r1.saldo_dias)
#r1.CalculoDecimoTerceiro()
#print(r1.dterceiro)
#rr1 = r1.CalculoTotalRescisao()

#print("%d/12 avos de ferias no valor de R$ %.2f reais" % (r1.avosFerias, r1.feriasproporcionais) )
#print(r1.difdatasFerias.days)

#print(rr1)
#hoje = date.today()
#print(hoje.strftime("%Y"))