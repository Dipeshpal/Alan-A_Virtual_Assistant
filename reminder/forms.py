from django import forms

class HomeForm4(forms.Form):
	date = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'DD/MM/YYYY',
			'id' : 'user_input'
		}
	))
	time = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'HH:MM',
			'id' : 'user_input'
		}
	))
	message = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Note or Message',
			'id' : 'user_input'
		}
	))


