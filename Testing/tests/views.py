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


class TestsListView(ListView):
    model = Test
    template_name = 'tests/tests_list.html'
    context_object_name = 'tests'
