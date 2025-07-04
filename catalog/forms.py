from django.forms import ModelForm
from catalog.models import Product
from django.core.exceptions import ValidationError


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['product_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название продукта'
        })
        self.fields['product_description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
        })
        self.fields['product_image'].widget.attrs.update({
            'class': 'form-control',
            'type': 'image'
        })
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',

        })
        self.fields['product_price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену продукта'
        })

    def clean_product_price(self):
        price = self.cleaned_data.get('product_price')
        if price is not None and price < 0:
            raise ValidationError('Цена не должна быть отрицательной')
        return price

