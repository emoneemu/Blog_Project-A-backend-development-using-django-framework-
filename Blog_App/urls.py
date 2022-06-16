from django.urls import path
from . import views

app_name = 'Blog_App'

urlpatterns = [
    path('',views.Blog_List,name='Blog_List'),
]
