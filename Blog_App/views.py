from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import View,CreateView,UpdateView,ListView,DetailView,TemplateView,DeleteView
from Blog_App.models import Blog,Comment,Likes
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Blog_App.forms import CommentForm
import uuid

# Create your views here.


#******* VERY VERY IMPORTANT!!!!!!******
#class based view er khetre @login_required use korle hobe na amader use korte hobe mixin
#we have to import mixin in that reason
#@login_required only used hoy functionbased view er khetre

#def Blog_List(request):
#    return render(request,'Blog_App/Blog_List.html',context={})

class Edit_Blog(LoginRequiredMixin,UpdateView):
    model = Blog
    fields = ('blog_title','blog_content','blog_image')
    template_name = 'Blog_App/Edit_Blog.html'

    def get_success_url(self,**kwargs):
        return reverse_lazy('Blog_App:Blog_Details',kwargs={'slug':self.object.slug})

class My_Blog(LoginRequiredMixin, TemplateView):
    template_name = 'Blog_App/My_Blog.html'

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
    queryset = Blog.objects.order_by('-publish_date')

@login_required
def Blog_Details(request,slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()
    already_liked = Likes.objects.filter(blog=blog,user=request.user)
    if already_liked:
        liked=True
    else:
        liked = False
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('Blog_App:Blog_Details',kwargs={'slug':slug}))

    return render(request,'Blog_App/Blog_Details.html',context={'blog':blog, 'comment_form':comment_form,'liked':liked})

@login_required
def liked(request,pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog,user=user)
    if not already_liked:
        liked_post =Likes(blog=blog,user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('Blog_App:Blog_Details',kwargs={'slug':blog.slug}))


@login_required
def unliked(request,pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog,user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('Blog_App:Blog_Details',kwargs={'slug':blog.slug}))
