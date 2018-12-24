from django import forms

from url.models import URL


class URL_Form(forms.ModelForm):

    user_url = forms.URLField()

    class Meta:
        model = URL
        fields = '__all__'
        labels = {
            'user_email': '(Optional) Email:',
        }
