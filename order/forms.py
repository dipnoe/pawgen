from django.forms import ModelForm

from main.forms import StyleFormMixin
from order.models import Application


class ApplicationForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Application
        exclude = ('owner',)

    def clean(self):
        cleaned_data = super().clean()
        specie = cleaned_data.get('specie')
        if specie:
            cleaned_data['specie'] = specie.lower()
        return cleaned_data
