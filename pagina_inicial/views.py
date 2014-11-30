from django.shortcuts import render
# Create your views here.

def PaginaInicial(request):
	context = {}
	template = 'pagina-inicial.html'
	return render(request,template,context,)

def Novidades(request):
	context = {}
	template = 'novidades.html'
	return render(request,template,context,)