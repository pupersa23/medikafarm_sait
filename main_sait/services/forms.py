from django import forms


class ArendaFlgForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    email_address = forms.EmailField(max_length=150)
    phone_number = forms.CharField(max_length=50)
    title = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea,
                              max_length=2000)
