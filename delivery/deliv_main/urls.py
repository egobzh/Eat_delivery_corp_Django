from django.urls import path
from . import views

urlpatterns = [path('', views.index.as_view(),name='index'),path('history', views.history.as_view(),name='history'),path('ondate', views.ondate.as_view(),name='ondate'),path('<int:num>', views.indexnum.as_view(),name='indnum')]