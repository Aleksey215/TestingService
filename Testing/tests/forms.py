from django import forms

from .models import Answer


class AnswerForm(forms.ModelForm):
    """
    Создание формы для выбора ответа
    """

    class Meta:
        model = Answer
        fields = ('selected',)

        widgets = {
            # поле "автор" заполнится автоматически
            'selected': forms.CheckboxInput(),
        }
