from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import View,CreateView,UpdateView,ListView,DetailView,TemplateView,DeleteView
from Blog_App.models import Blog,Comment,Likes
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
# Create your views here.


#******* VERY VERY IMPORTANT!!!!!!******
#class based view er khetre @login_required use korle hobe na amader use korte hobe mixin
#we have to import mixin in that reason
#@login_required only used hoy functionbased view er khetre

#def Blog_List(request):
#    return render(request,'Blog_App/Blog_List.html',context={})


class CreateBlog(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'Blog_App/Create_Blog.html'
    fields = ('blog_title','blog_content','blog_image')

    def form_valid(self,form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ","-")+"-"+str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))
class BlogList(ListView):
    context_object_name ='blogs'
    model = Blog
    template_name = 'Blog_App/Blog_List.html'
