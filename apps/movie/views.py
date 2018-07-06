from django.shortcuts import render


# Create your views here.

def home_page(request):
    return render(request, 'home/movie_list.html')


def movie_details(request):
    return render(request, 'home/movie_details.html')
