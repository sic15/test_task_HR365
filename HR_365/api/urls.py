from django.urls import path

from . import views

urlpatterns = [
    path('rates/from=<fr>&to=<to>&value=<value>', views.converter, name='converter'),
]