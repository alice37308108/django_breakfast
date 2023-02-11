from django import forms

from .models import Breakfast


class BreakfastForm(forms.ModelForm):
    class Meta:
        # どのモデルをフォームにするか指定
        model = Breakfast
        # そのフォームの中から表示するフィールドを指定
        fields = ('date', 'hours_of_sleep', 'breakfast', 'sleep_quality', 'feeling', 'sweet', 'memo',)

