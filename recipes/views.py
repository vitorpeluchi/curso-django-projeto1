from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html')
    # return HTTP response


# Create your views here.
