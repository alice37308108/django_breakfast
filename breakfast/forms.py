from django import forms
from django.core.exceptions import ValidationError

from .models import Breakfast


class BreakfastModelForm(forms.ModelForm):
    class Meta:
        model = Breakfast
        fields = "__all__"

    def clean_breakfast(self):
        breakfast = self.cleaned_data['breakfast']
        if breakfast == '干し芋':
            raise ValidationError('干し芋はご飯ではなくておやつです！！')
        return breakfast

    def clean(self):
        cleaned_data = super().clean()
        breakfast = cleaned_data.get('breakfast')
        sweet = cleaned_data.get('sweet')

        if breakfast is not None and sweet is not None:
            if breakfast == sweet:
                raise ValidationError('朝食とおやつが一緒なのはどうなのでしょうか？')
            return cleaned_data

