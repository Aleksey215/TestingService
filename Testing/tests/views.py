from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Answer, Question, Set, Test, Theme


class SetListView(ListView):
    pass

