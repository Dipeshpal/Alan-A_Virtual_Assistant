from django import forms

class HomeForm2(forms.Form):
	post = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Your Text Here',
			'id' : 'user_input'
		}
	))
