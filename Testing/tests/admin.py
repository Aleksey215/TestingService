from django.contrib import admin
import nested_admin

from .models import Answer, Question, Set, Test, Theme


class AnswerInline(nested_admin.NestedStackedInline):
    model = Answer
    extra = 0


class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    inlines = [AnswerInline]
    extra = 0


class TestInline(nested_admin.NestedStackedInline):
    model = Test
    inlines = [QuestionInline]
    extra = 0


class SetAdmin(nested_admin.NestedModelAdmin):
    inlines = [TestInline]


admin.site.register(Theme)
admin.site.register(Set, SetAdmin)
