from django import forms
from .models import User

from django.core.exceptions import ValidationError


class SignupForm(forms.ModelForm):
	first_name = forms.CharField(max_length=20, required=True, help_text='Required')
	last_name = forms.CharField(max_length=20, required=True, help_text='Required')
	email = forms.CharField(max_length=50, required=True, help_text='Required')
	
	class Meta:
		model = User
		fields = [
		'first_name',
		'last_name', 
		'email'
		]

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if email and User.objects.filter(email=email).count()>0:
			raise forms.ValidationError("This email address is already in use")
		return email


