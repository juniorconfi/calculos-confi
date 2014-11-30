from django.shortcuts import render
# Create your views here.

from django.shortcuts import render_to_response
from multiprocessing.sharedctypes import template
from .forms import formCalculoFerias
from .calculo_ferias import Ferias

def index(request):
	# Se esta é uma solicitação GET que precisamos para processar os dados do formulário
	if request.method == 'GET':
		#  Criar uma instância do formulário e preenchê-lo com dados do pedido:
		fr1 = formCalculoFerias(request.GET or None)
		if fr1.is_valid():
			# Processar os dados em form.cleaned_data como exigido
			sal = fr1.cleaned_data['salario_bruto']
#			dep = fr1.cleaned_data['nro_dependentes']
#			horaextra = fr1.cleaned_data['hrs_extras']
#			qtdhorasadicnoturno = fr1.cleaned_data['hrs_adicional_noturno']
			rc1 = Ferias(sal)
			rc1.ImprimeDadosFerias()
			#Testar os calculos - saida no shell do servidor
#			print(c1.CalculoSalarioLiquido())
			# ...
			# Redirecionar para uma nova URL:
			return render(request,'resultado-calculos-ferias.html', {'f1': rc1})
		# se o metodo for diferente de GET criar um formulario em branco
	else:
		fr1 = formCalculoFerias()
	return render(request, 'calculo-ferias.html', {'form' : fr1})
