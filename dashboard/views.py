from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
import facebook as fb
from .facebook_credentials import Credentials

# Create your views here.

@login_required
def dashboard(request):
    context = {
        'user': request.user
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def posts(request):
    context = {
        'posts' : data_access()
    }
    return render(request, 'dashboard/posts.html', context)


def data_access():
    posts = []
    cred = Credentials()
    try:
        graph = fb.GraphAPI(cred.get_token())
        page = graph.get_object('826799967663341', fields='posts{comments, picture, message}')

        for data in page['posts']['data']:
            if 'picture' in data.keys():
                posts.append(data)

        return posts

    except:
        return posts

   

    
    