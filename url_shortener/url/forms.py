from django import forms

from url.models import URL


class URL_Form(forms.ModelForm):

    class Meta:
        model = URL
        fields = '__all__'