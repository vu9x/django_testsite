from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Название')
    content = forms.CharField(label='Текст', required=False)
    is_published = forms.BooleanField(label='Опубликовано', initial=True)
    category = forms.ModelChoiceField(empty_label='Выберите категорию', label='Категория', queryset=Category.objects.all())

