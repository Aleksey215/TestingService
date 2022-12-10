from django.urls import path

from .views import SetsListView, SetDetail, TestsListView

urlpatterns = [
    path('', SetsListView.as_view(), name='sets_list'),
    path('tests/<int:pk>/', SetDetail.as_view(), name='set_detail'),
    path('tests/', TestsListView.as_view(), name='tests_list'),
]
