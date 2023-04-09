from django.urls import path
from .views import (
    index
)


app_name = 'Base'

urlpatterns = [

    path('',index,name='index')
]