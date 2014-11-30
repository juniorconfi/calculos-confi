from django import forms
# FORMS DA RESCISÃO
from datetime import date
from django.forms.extras.widgets import SelectDateWidget


class formCalculoRescisao(forms.Form):
	hoje = date.today()
	#ano_atual = int(hoje.strftime("y"))
	anos = range(1990,2015)
	#BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
	#hoje = datetime.date.today()
	LISTA_SIM_NAO = (('Sim', 'Sim'), ('Nao','Nao'))
	TIPO_DEMISSAO = (('Sem Justa Causa','Sem Justa Causa'),('Fim do contrato de experiencia','Fim do contrato de experiencia'),('Justa Causa','Justa Causa'))
	TIPO_AVISO = (('Trabalhado','Trabalhado'),('Indenizado','Indenizado'))
	
	
	#birth_year = forms.DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
	dt_admissao = forms.DateField(label="Data de admissao", widget=SelectDateWidget(years=anos), initial=hoje)
	dt_saida = forms.DateField(label="Data da saida", widget=SelectDateWidget(years=anos),initial=hoje)
	tipo_demissao = forms.ChoiceField(label="Tipo?", choices=TIPO_DEMISSAO)
	tipo_aviso = forms.ChoiceField(label="Aviso Previo", choices=TIPO_AVISO)
	ferias_vencidas = forms.ChoiceField(label="Ferias Vencidas", choices=LISTA_SIM_NAO)
	ult_salario = forms.FloatField(label="Salario")
	