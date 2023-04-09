from django.urls import path
from .views import (loginpage
,register
,logoutUser

,per_page_view)

app_name = 'User_Profile'

urlpatterns = [
    path('login/', loginpage, name='login'),
    path('register/', register, name='register'),
    path('logout/',logoutUser,name='logout'),
    path("per_page", per_page_view, name="per_page")
]