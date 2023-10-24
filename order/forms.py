from django.forms import ModelForm, forms

from main.forms import StyleFormMixin
from order.models import Application


class ApplicationForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Application
        exclude = ('owner', 'is_submitted',)

    def clean(self):
        cleaned_data = super().clean()
        specie = cleaned_data.get('specie')
        if specie:
            cleaned_data['specie'] = specie.lower()
        return cleaned_data

    def clean_microchip_number(self):
        cleaned_data = self.cleaned_data.get('microchip_number')
        if cleaned_data:
            if not cleaned_data.isdigit() and len(cleaned_data) != 15:
                raise forms.ValidationError('Неккоректный номер чипа. Чип должен состоять из 15 цифр')
            return cleaned_data
