from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Answer, Question, Set, Test, Theme


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
        context['first_question'] = Question.objects.filter(test=id)[0]
        context['second_question'] = Question.objects.filter(test=id)[0]
        context['answers'] = Answer.objects.all()
        return context


class QuestionDetail(DetailView):
    model = Question
    template_name = 'tests/question_detail.html'
