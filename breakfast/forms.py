from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import Textarea
from django.utils import timezone

from .models import Breakfast


class BreakfastModelForm(forms.ModelForm):
    breakfast = forms.CharField(label='朝ごはん',max_length=10)

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

    # def clean_feeling(self):  # 単体のバリデーションを行う場合はclean_フィールド名()をオーバーライドする
    #     feeling = self.cleaned_data['feeling']
    #     if feeling < 1 or feeling > 5:
    #         raise ValidationError('1以上5以下の値を入力してください。')
    #     return feeling

# class BreakfastModelForm(forms.ModelForm):
#     feeling = forms.IntegerField(label='今日の気分', min_value=1, max_value=5)
#
#     def clean_feeling(self):  # 単体のバリデーションを行う場合はclean_フィールド名()をオーバーライドする
#         feeling = self.cleaned_data['feeling']
#         if feeling < 1 or feeling > 5:
#             raise ValidationError('1以上5以下の値を入力してください。')
#         return feeling
#
#     def clean(self):
#         cleaned_data = super().clean()
#         hours_of_sleep = cleaned_data.get('hours_of_sleep')
#         sleep_quality = cleaned_data.get('sleep_quality')
#         if hours_of_sleep is not None and sleep_quality is not None:
#             if hours_of_sleep < 3 and sleep_quality > 2:
#                 raise ValidationError('あまり寝れなかったのに睡眠の質がいいわけないじゃん！')
#         return cleaned_data
#
#     # NG例
#     def clean(self):  # 複数フィールド間のバリデーションを行う場合はclean()をオーバーライドする　単体では使えないことはないけど使わない
#         cleaned_data = super().clean()
#         feeling = cleaned_data.get('feeling')
#         if feeling < 1 or feeling > 5:
#             raise ValidationError('1以上5以下の値を入力してください。')
#         return cleaned_data


# class BreakfastForm(forms.Form):
#     date = forms.DateTimeField(label='日付')
#     hours_of_sleep = forms.IntegerField(label='睡眠時間')
#     breakfast = forms.CharField(label='朝食')
#     sleep_quality = forms.IntegerField(label='睡眠の質')
#     feeling = forms.IntegerField(label='気分')
#     sweet = forms.CharField(label='お菓子')
#     memo = forms.CharField(label='メモ')
#
#     def clean_date(self):
#         date = self.cleaned_data['date']
#         if date > timezone.now():
#             raise ValidationError('未来の日付は入力できません。')
#         return date
#
#     def clean_hours_of_sleep(self):
#         hours_of_sleep = self.cleaned_data['hours_of_sleep']
#         if hours_of_sleep < 0:
#             raise ValidationError('0以上の値を入力してください。')
#         elif hours_of_sleep > 24:
#             raise ValidationError('24以下の値を入力してください。')
#         return hours_of_sleep
#
#     def clean_sleep_quality(self):
#         sleep_quality = self.cleaned_data['sleep_quality']
#         if sleep_quality < 0:
#             raise ValidationError('0以上の値を入力してください。')
#         elif sleep_quality > 5:
#             raise ValidationError('5以下の値を入力してください。')
#         return sleep_quality
