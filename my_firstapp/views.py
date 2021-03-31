from django.shortcuts import render
from .models import Post


# Create your views here.



def Home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'my_firstapp/Home.html', context)

def About(request):
    return render( request, 'my_firstapp/About.html', {'title' : 'About'} )


