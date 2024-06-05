from django.shortcuts import render

from foodapp.models import *


# Create your views here.
def foodview(request):
    if request.method == "POST":
        data = request.POST

        image = request.FILES.get('food_image')
        name = data.get('food_name')
        description = data.get('food_description')

        Food.objects.create(
            food_image = image,
            food_name = name,
            food_description = description
        )

    return render(request, 'food.html')