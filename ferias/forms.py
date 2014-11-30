from django import forms



class formCalculoFerias(forms.Form):
	#escolha_abono = ("Sim", "Nao")
	salario_bruto = forms.FloatField(label="Salario Bruto")
	vr_comissoes = forms.FloatField(label="Valor Vale Transporte", initial=0)
	hrs_extras = forms.IntegerField(label="Horas Extras", initial=0)
	nro_dependentes = forms.IntegerField(label="Dependentes" , initial=0)
	#abono_pecuniario = form.CharField("Vender 1/3 (abono pecuniario)", choice=escolha_abono)
	