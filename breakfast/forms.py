from django import forms


# class BreakfastForm(forms.Form):
#     date = forms.DateField()
#     hours_of_sleep = forms.IntegerField()
#     breakfast = forms.CharField(max_length=200)
#     sleep_quality = forms.IntegerField()
#     feeling = forms.IntegerField()
#     sweet = forms.CharField(max_length=200, required=False)
#     memo = forms.CharField(max_length=200, required=False)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control'


from django import forms

from .models import Breakfast


class BreakfastForm(forms.ModelForm):
    class Meta:
        # どのモデルをフォームにするか指定
        model = Breakfast
        # そのフォームの中から表示するフィールドを指定
        fields = ('date', 'hours_of_sleep', 'breakfast', 'sleep_quality', 'feeling', 'sweet', 'memo',)

    # フォームを綺麗にするための記載
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
