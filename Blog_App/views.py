from django.shortcuts import render

# Create your views here.

def Blog_List(request):
    return render(request,'Blog_App/Blog_List.html',context={})
