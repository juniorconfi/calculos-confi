from django import forms

class formCalculoSalarios(forms.Form):
	salario_bruto = forms.FloatField(label="Salario Bruto")
	#nro_dependentes = forms.IntegerField(label="Dependentes" , initial=0)
	hrs_extras = forms.IntegerField(label="Horas Extras", initial=0)
	hrs_adicional_noturno = forms.IntegerField(label="Adicional Noturno", initial=0)
	dias_vtransporte = forms.IntegerField(label="Dias de vale Transporte", initial=0)
	vr_vtransporte = forms.FloatField(label="Valor Vale Transporte", initial=0)
	#qtd_faltas = forms.IntegerField(label="Quantidade de Faltas", initial=0)
	#descontos_outros = forms.FloatField(label="Outros Descontos", initial=0)