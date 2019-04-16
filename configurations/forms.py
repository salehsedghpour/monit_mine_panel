from django import forms
class addNewMiner(forms.Form):
    miner_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'id': 'miner_name'
            }
        ),
        label=False,
        required=False
    )
    miner_ip = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'id': 'miner_ip'
            }
        ),
        label=False,
        required=False
    )
    miner_user = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'id': 'miner_user'
            }
        ),
        label=False,
        required=False
    )
    miner_pass = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'id': 'miner_pass'
            }
        ),
        label=False,
        required=False
    )