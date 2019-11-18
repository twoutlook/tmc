from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class PartForm(forms.Form):
    yr = forms.IntegerField(label='年')
    mo = forms.IntegerField(label='月')
    cutoff = forms.DateField(label='截止日期')