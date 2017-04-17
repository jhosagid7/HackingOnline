from django import forms

class cmsmap(forms.Form):

	website = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Introduce Pagina Web'}), max_length=50, label='', required=True)