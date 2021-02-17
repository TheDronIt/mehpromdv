from .models import Message
from django.forms import ModelForm, TextInput, EmailInput, Textarea 

class MessageForm(ModelForm):
	class Meta:
		model = Message
		fields = ['FIO', 'phone', 'email', 'text']

		widgets = {
			"FIO": TextInput(attrs={
					'class': 'form-smalltext form-text',
					'placeholder': 'ФИО'
				}),
			"phone": TextInput(attrs={
					'class': 'form-smalltext form-text',
					'placeholder': 'Номер телефона'
				}),
			"email": EmailInput(attrs={
					'class': 'form-smalltext form-text',
					'placeholder': 'Почта'
				}),
			"text": Textarea(attrs={
					'class': 'form-bigtext form-text',
					'placeholder': 'Сообщение'
				}),
		}