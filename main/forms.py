from django.forms import ModelForm

from main.models import Category, Service


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CategoryForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ServiceForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
