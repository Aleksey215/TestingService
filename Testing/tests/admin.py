from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet, ModelForm
# for nested inline
import nested_admin

from .models import Answer, Question, Set, Test, Theme


class AnswerAdminForm(ModelForm):

    class Meta:
        model = Answer
        fields = '__all__'

    # def clean_correct(self):
    #     correct = self.cleaned_data['correct']
    #     print(correct)
    #     return correct

    def clean_question(self):
        question = self.cleaned_data['question']
        corr = self.cleaned_data['correct']

        return question


class AnswerInline(nested_admin.NestedStackedInline):
    """
    Inline for question
    """
    model = Answer
    extra = 0
    form = AnswerAdminForm


class QuestionInline(nested_admin.NestedStackedInline):
    """
    Inline for test
    """
    model = Question
    inlines = [AnswerInline]
    extra = 0


class TestInline(nested_admin.NestedStackedInline):
    """
    Inline for test set
    """
    model = Test
    inlines = [QuestionInline]
    extra = 0


class SetAdmin(nested_admin.NestedModelAdmin):
    """
    For creation test set with nested tests, questions and answers
    """
    inlines = [TestInline]


# Register models for admin panel
admin.site.register(Theme)
admin.site.register(Set, SetAdmin)
