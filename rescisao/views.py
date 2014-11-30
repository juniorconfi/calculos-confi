from django.shortcuts import render
# Create your views here.

# ***************   VIEWS DE CALCULOS DA RESCISÃO **************

from django.shortcuts import render_to_response
from multiprocessing.sharedctypes import template
from .forms import formCalculoRescisao
from .calculo_rescisao import Rescisao
from datetime import date

def index(request):
	# Se esta é uma solicitação GET que precisamos para processar os dados do formulário
	if request.method == 'GET':
		#  Criar uma instância do formulário e preenchê-lo com dados do pedido:
		fr1 = formCalculoRescisao(request.GET or None)
		if fr1.is_valid():
			# Processar os dados em form.cleaned_data como exigido
			dtadm = fr1.cleaned_data['dt_admissao']
			dtsai = fr1.cleaned_data['dt_saida']
			ultsal = fr1.cleaned_data['ult_salario']
			rc1 = Rescisao(dtadm,dtsai,ultsal)
			rc1.ImprimeDadosRescisao()
			
			print('Saida pelo Shell Abaixo')
			print(rc1.rSaldo)


			return render(request, 'resultado-calculos-rescisao.html', {'f1': rc1 })
	else:
		fr1 = formCalculoRescisao()

	return render(request, 'calculos-rescisao.html', {'form' : fr1})
