from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .facebook_graph_api_explorer import FetchData

# Create your views here.

data = FetchData()

@login_required
def dashboard(request):
    context = {
        'user': request.user
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def posts(request):
   
    context = {
        'posts': data.fetch_all_posts("826799967663341")
    }
    return render(request, 'dashboard/posts.html', context)


@login_required
def post_view(request, id):
    context = {
        'post': data.fetch_one_post(id)
    }
    
    return render(request, 'dashboard/postview.html', context)




   

    
    