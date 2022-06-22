from django.urls import path
from Blog_App import views

app_name = 'Blog_App'

urlpatterns = [
    path('',views.BlogList.as_view(),name='Blog_List'),
    path('write/',views.CreateBlog.as_view(),name='Create_Blog'),
    path('details/<slug>/',views.Blog_Details,name='Blog_Details'),
    path('liked/<pk>/',views.liked, name='liked_post'),
    path('unliked/<pk>/',views.unliked, name ='unliked_post'),
    path('My-Blog',views.My_Blog.as_view(),name='My_Blog'),
    path('Edit-Blog/<pk>',views.Edit_Blog.as_view(),name='Edit_Blog')
]
