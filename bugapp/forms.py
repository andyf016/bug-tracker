from django import forms
from bugapp.models import Ticket
from myuser.models import CustomUser

class TicketForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['title', 'description']
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)