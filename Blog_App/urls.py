from django.urls import path
from . import views

app_name = 'Blog_App'

urlpatterns = [
    path('',views.BlogList.as_view(),name='Blog_List'),
    path('write/',views.CreateBlog.as_view(),name='Create_Blog'),
]
