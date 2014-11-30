class CalculoSalarioLiquido(object):

	def __init__(self,salbruto, hrsextras, qtdhrsnot, qtdvt, vrvt):
		self.salbruto = salbruto
		#self._nrdep = nrdep
		self.hrsextras = hrsextras
		self.qtdhrsnot = qtdhrsnot
		self.qtdvt = qtdvt
		self.vrvt = vrvt
    
#	def CalculoDependentes(self):
#		self.totaldependentes = self.nrdependentes * 20
#		return self.totaldependentes

	def CalculoHoraExtra(self):
		self.total_hrsextras = self.hrsextras * ( 1.5 * ( self.salbruto/220))
		return self.total_hrsextras
    
	def CalculoAdicionalNoturno(self):
		self.totaladicnoturno = self.qtdhrsnot * (1.2 * ( self.salbruto/220))
		return self.totaladicnoturno
    
	def CalculoVTransporteTotal(self):
		self.totalvt = self.qtdvt * self.vrvt
		return self.totalvt

	def CalculoInss(self):
		if self.salbruto <= 1317.07:
			self.vrInssEmpregado = 0.08 * self.salbruto
			self.indiceInss = "8%"
		elif self.salbruto <= 2195.12:
			self.vrInssEmpregado = 0.09 * self.salbruto
			self.indiceInss = "9%"
		elif self.salbruto <= 4390.24:
			self.vrInssEmpregado = 0.11 * self.salbruto
			self.indiceInss = "11%"
		else:
			self.vrInssEmpregado = 0.11 * 4390.24
			self.indiceInss = "11%"
		return self.vrInssEmpregado, self.indiceInss

	def CalculoTotalSalarioLiquido(self):
		self.proventos = self.salbruto + self.CalculoHoraExtra() + self.CalculoAdicionalNoturno() + self.CalculoVTransporteTotal()
		self.rInss = self.CalculoInss()
		self.indiceINSS = self.rInss[1]
		self.vrInss = self.rInss[0]
		self.descontos = self.vrInss
		self.salLiquido = self.proventos - self.descontos
		return ('%.2f' % self.salLiquido), ('%.2f' % self.proventos), ('%.2f' % self.descontos), self.indiceINSS

'''		
sal = float(input('Digite o Salario: '))
horaextra = float(input('Digite a Quantidade de Horas Extras: '))
qtdhorasadicnoturno = float(input('Quantas horas de adicional noturno: '))
qtdVTrasnporte = float(input('Quantidade de Vales Transportes: '))
vrVTransporte = float(input('O valor do vale Transporte: '))
'''
c1 = CalculoSalarioLiquido(2097,0, 0, 0, 0)
print('O Valor do Salario Liquido: ' , c1.CalculoTotalSalarioLiquido())
#print(c1.CalculoSalarioLiquido(sal,horaextra))
