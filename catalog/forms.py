from django import forms
from django.core.validators import ValidationError

from .models import Product, Category

BAD_WORDS = ('казино', 'биржа', 'обман', 'криптовалюта', 'дешево', 'полиция', 'крипта', 'бесплатно', 'радар')


class CatalogCreateForm(forms.ModelForm):
    category = forms.CharField(max_length=150, label='Категория', error_messages={'required': 'Это поле обязательно'})

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'price']
        error_messages = {'category': {'required': 'Это поле обязательно'}}
        for field in fields:
            error_messages[field] = {'required': 'Это поле обязательно'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.category:
            self.initial['category'] = self.instance.category.name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Вы не можете платить покупателям')
        return price

    def clean(self):
        cleaned_data = super().clean()
        name = str(cleaned_data.get('name'))
        description = str(cleaned_data.get('description'))
        category = str(cleaned_data.get('category'))

        for bad_word in BAD_WORDS:
            if bad_word in name.lower():
                self.add_error('name', f'\"{bad_word}\" – плохое слово')
            if bad_word in description.lower():
                self.add_error('description', f'\"{bad_word}\" – плохое слово')
            if bad_word in category.lower():
                self.add_error('category', f'\"{bad_word}\" – плохое слово')
