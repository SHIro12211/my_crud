from django.urls import path

from . import views


urlpatterns = [
    #
    path('add/', views.PersonFormViews.add, name='add'),

]
