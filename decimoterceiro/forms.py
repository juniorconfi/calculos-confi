from django import forms
from django.forms.extras.widgets import SelectDateWidget
from datetime import date

class formCalculoDecimoTerceiro(forms.Form):
	hoje = date.today()
	ano = ('2014','2014')
	dt_admissao = forms.DateField(label="Data de admissao", widget=SelectDateWidget(years=ano), initial=hoje )
	salario_bruto = forms.FloatField(label="Salario bruto")
	vr_comissoes = forms.FloatField(label="Comissoes (Valor Medio)", initial=0)
	vr_horas_extras = forms.FloatField(label="Horas Extras (Valor medio)", initial=0)
	nro_dependentes = forms.IntegerField(label="Dependentes" , initial=0)
	
	