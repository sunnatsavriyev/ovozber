from django.urls import path
from .views import OvozApiView, OvozDetail

urlpatterns = [
    path('',OvozApiView.as_view(), name='vote-list'),
    path("<int:pk>/",OvozDetail.as_view(), name='vote-detail')
]