from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .sentiment_analysis import SentimentAnalysis
from .facebook_graph_api_explorer import FetchData
from .models import Page
import os
import csv

# Create your views here.

data = FetchData()
analysis = SentimentAnalysis()

@login_required
def dashboard(request):
    pages = Page.objects.filter(page_user=User.objects.filter(username=request.user)[0])
    context = {
        'user': request.user,
        'pages': pages
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def searchpage(request):
    if request.method == 'POST':
        page_id = request.POST.get('pageid')
        page_user = User.objects.filter(username=request.user)[0]

        if not Page.objects.filter(page_id=page_id, page_user=page_user):
            page_data = data.fetch_page_data(page_id)
            Page.objects.create(page_id=page_id, page_name=page_data['name'], page_picture=page_data['picture']['data']['url'], page_user=page_user)
        

    return posts(request, page_id)

    

@login_required
def posts(request, page_id):
   
    context = {
        'posts': data.fetch_all_posts(page_id)
    }
    return render(request, 'dashboard/posts.html', context)


@login_required
def post_view(request, id):
    post = data.fetch_one_post(id)
   
        

    context = {
        'post': post
        # 'prediction': prediction,
        # 'p_count': p_count,
        # 'n_count': n_count,
        # 'accuracy': accuracy,
    }
    
    return render(request, 'dashboard/postview.html', context)

def analyze_post(request):
    if request.is_ajax and request.method == "GET":
        comments = request.GET.getlist('comments[]')
        p_count = 0
        n_count = 0
    
        analysis.create_model()
        accuracy = str(round(analysis.get_accuracy() * 100)) + " %"
        prediction = []

        
        if len(comments) == 1:
            prediction = [[comments[0], analysis.predict_one_review(comments[0])]]

        else:
            prediction = analysis.predict_many_reviews(comments)

            for s_count in prediction:
                if s_count[1] == "Positive":
                    p_count += 1
                else:
                    n_count += 1
        return JsonResponse({
            "p_count": p_count,
            "n_count": n_count,
            "accuracy": accuracy,
            "prediction": prediction
            }, status=200)
    else:
        return JsonResponse({"error": "An error occurred"}, status=400)


def generate_csv(request):
    if request.is_ajax and request.method == "GET":
        predictions = []
        for i in range(int(request.GET['predLength'])):
            prediction = request.GET.getlist(f'prediction[{i}][]')
            predictions.append(prediction)
        
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

        with open(desktop + '\data.csv', 'w+', newline="") as file:
            fieldnames = ['comment', 'prediction']

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for pred in predictions:
                writer.writerow({'comment': pred[0], 'prediction': pred[1]})

            return JsonResponse({
                "success": "Successfully generataed the csv file"
            }, status=200)
    else:
        return JsonResponse({"error": "An error occurred"}, status=400)


    
