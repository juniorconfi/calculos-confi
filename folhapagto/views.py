from django.shortcuts import render
# Create your views here.

from django.shortcuts import render_to_response
from multiprocessing.sharedctypes import template
from .forms import formCalculoSalarios
from .calculo_salario import CalculoSalarioLiquido
#def index(request):
#	context = {}
#	template = 'folha-pagamento.html'
#	return render(request,template,context)

def index(request):
	# Se esta é uma solicitação GET que precisamos para processar os dados do formulário
	if request.method == 'GET':
		#  Criar uma instância do formulário e preenchê-lo com dados do pedido:
		fr1 = formCalculoSalarios(request.GET or None)
		if fr1.is_valid():
			# Processar os dados em form.cleaned_data como exigido
			sal = fr1.cleaned_data['salario_bruto']
			#dep = fr1.cleaned_data['nro_dependentes']
			horaextra = fr1.cleaned_data['hrs_extras']
			qtdhradnot = fr1.cleaned_data['hrs_adicional_noturno']
			qtddiasVt = fr1.cleaned_data['dias_vtransporte']
			vrVt = fr1.cleaned_data['vr_vtransporte']

			cf1 = CalculoSalarioLiquido(sal, horaextra, qtdhradnot, qtddiasVt, vrVt)
			#Testar os calculos - saida no shell do servidor
			cf1.CalculoTotalSalarioLiquido()
			# ...
			# Redirecionar para uma nova URL:
			return render(request,'resultado-calculos-folha-pagamento.html', {'rf1': cf1})
		# se o metodo for diferente de GET criar um formulario em branco
	else:
		fr1 = formCalculoSalarios()
	return render(request, 'folha-pagamento.html', {'form' : fr1},)