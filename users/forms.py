from django import forms
from datetime import datetime,timedelta


now = datetime.now().date()

class SaladForm(forms.Form):
    CHOICES = [
        (True, '샐러드 먹기'),
        (False, '샐러드 안 먹기'),
    ]
           
    choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
