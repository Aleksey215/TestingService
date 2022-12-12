from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Answer, Question, Set, Test, Theme
from .forms import AnswerForm


class SetsListView(ListView):
    model = Set
    context_object_name = 'sets'
    template_name = 'tests/sets_list.html'


class SetDetail(DetailView):
    model = Set
    template_name = 'tests/set_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        context['tests'] = Test.objects.filter(set=id)
        return context


class TestDetailView(DetailView):
    model = Test
    template_name = 'tests/test_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        question = Question.objects.filter(test=id, answered=False)[0]
        context['active_question'] = question
        context['answers'] = Answer.objects.filter(question=question)
        context['answer_form'] = AnswerForm()
        return context


class QuestionDetail(DetailView):
    model = Question
    template_name = 'tests/question_detail.html'


class Questions(ListView):
    model = Question
    template_name = 'tests/questions.html'
    context_object_name = 'questions'
