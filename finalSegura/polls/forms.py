from django import forms
from polls.models import Perfil

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirmar_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Perfil
        fields = ['username', 'first_name', 'last_name', 'email', 'Token', 'chatID', 'password', 'confirmar_password']
        db_table = 'polls_perfil'
        help_texts = {k:"" for k in fields }