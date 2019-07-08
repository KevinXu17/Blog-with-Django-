from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Your title'}))
    description = forms.CharField(widget=forms.Textarea(
        attrs= {
        'rows': 20,
        'cols': 30
    }))
    email = forms.EmailField()
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'

        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if 'CFE' in title:
            return title
        else:
            raise forms.ValidationError("This is not a valid title")

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email



class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea(
        attrs= {
        'rows': 20,
        'cols': 30
    }))
    price = forms.DecimalField()