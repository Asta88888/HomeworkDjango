from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class UserRegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=35, required=False)
    username = forms.CharField(max_length=50, required=True)


    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone_number')
        if phone and not phone.isdigit():
            raise forms.ValidationError('Номер телефона должен состоять только из цифр')
        return phone


