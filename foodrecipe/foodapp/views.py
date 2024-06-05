from django.shortcuts import render


# Create your views here.
def foodview(request):
    return render(request, 'food.html')