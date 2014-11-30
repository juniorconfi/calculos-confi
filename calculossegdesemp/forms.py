from django import forms

class formCalculoSeguroDesemprego(forms.Form):
	dt_admissao = forms.DateField(label="Data de admissao")
	salario_bruto = forms.FloatField(label="Salario bruto")

	