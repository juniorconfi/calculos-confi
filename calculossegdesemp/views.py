from django.shortcuts import render
# Create your views here.

from django.shortcuts import render_to_response
from multiprocessing.sharedctypes import template
from .forms import formCalculoSeguroDesemprego

def index(request):
	# Se esta é uma solicitação GET que precisamos para processar os dados do formulário
	if request.method == 'GET':
		#  Criar uma instância do formulário e preenchê-lo com dados do pedido:
		fr1 = formCalculoSeguroDesemprego(request.GET or None)
		if fr1.is_valid():
			# Processar os dados em form.cleaned_data como exigido
			return render_to_response('resultado-calculos.html', {'f1': c1})
	else:
		fr1 = formCalculoSeguroDesemprego()
	return render(request, 'calculos-seguro-desemprego.html', {'form' : fr1})
