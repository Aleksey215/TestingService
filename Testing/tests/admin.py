from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet, ModelForm
# for nested inline
import nested_admin

from .models import Answer, Question, Set, Test, Theme


class AnswerInline(nested_admin.NestedStackedInline):
    """
    Inline for question
    """
    model = Answer
    extra = 0


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
