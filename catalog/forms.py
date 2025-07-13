from django.forms import ModelForm
from catalog.models import Product
from django.core.exceptions import ValidationError


FORBIDDEN_WORDS = [
    "казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"
]


MAX_IMAGE_SIZE = 5


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


    def contains_forbidden_words(self, text):
        if not text:
            return False
        text = text.lower()
        return any(word in text for word in FORBIDDEN_WORDS)


    def clean_product_name(self):
        name = self.cleaned_data.get('product_name')
        if self.contains_forbidden_words(name):
            raise ValidationError('Название содержит запрещенные слова')
        return name


    def clean_product_description(self):
        description = self.cleaned_data.get('product_description')
        if self.contains_forbidden_words(description):
            raise ValidationError('Описание содержит запрещенные слова')
        return description


    def clean_product_image(self):
        image = self.cleaned_data.get('product_image')
        if image:
            if image.size > MAX_IMAGE_SIZE * 1024 * 1024:
                raise ValidationError(f'Размер изображения не должен превышать {MAX_IMAGE_SIZE}')
            content_type = image.file.content_type
            if content_type not in ['jpeg','png']:
                raise ValidationError('Допустимые форматы изображения: JPEG и PNG')
        return image
