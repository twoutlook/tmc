from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class PhoneForm(forms.Form):
    phone = forms.CharField(label='Phone', max_length=11)