from django.shortcuts import render

def academy_articles_view(request):
    return render(request, 'academy_articles.html')