from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username:', widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Username',
            }
        ),)
    password = forms.CharField(label='Password:',widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-sm',
        'placeholder': 'Password',
    }))