from django.shortcuts import render
# Create your views here.

from django.shortcuts import render_to_response
from multiprocessing.sharedctypes import template
from .forms import formCalculoDecimoTerceiro
from.calculo_decimo import DecimoTerceiro

def index(request):
	# Se esta é uma solicitação GET que precisamos para processar os dados do formulário
	if request.method == 'GET':
		#  Criar uma instância do formulário e preenchê-lo com dados do pedido:
		fr1 = formCalculoDecimoTerceiro(request.GET or None)
		if fr1.is_valid():
			# Processar os dados em form.cleaned_data como exigido
			dtadm = fr1.cleaned_data['dt_admissao']
			salbruto = fr1.cleaned_data['salario_bruto']
			c1 = DecimoTerceiro(dtadm, salbruto)
			c1.ImprimeDadosDecimo()

			return render(request, 'resultado-calculos-decimo.html', {'f1': c1})
	else:
		fr1 = formCalculoDecimoTerceiro()
	return render(request, 'calculos-decimo-terceiro.html', {'form' : fr1})
