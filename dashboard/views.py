from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .sentiment_analysis import SentimentAnalysis
from .facebook_graph_api_explorer import FetchData

# Create your views here.

data = FetchData()
analysis = SentimentAnalysis()

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
    


    
