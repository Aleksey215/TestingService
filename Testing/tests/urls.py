from django.urls import path

from .views import SetsListView, SetDetail, TestDetailView, QuestionDetail, Questions

urlpatterns = [
    path('', SetsListView.as_view(), name='sets_list'),
    path('set/<int:pk>/', SetDetail.as_view(), name='set_detail'),
    path('/test/<int:pk>/', TestDetailView.as_view(), name='test_detail'),
    path('/question/<int:pk>/', QuestionDetail.as_view(), name='question'),
    path('questions/', Questions.as_view(), name='questions'),
]
