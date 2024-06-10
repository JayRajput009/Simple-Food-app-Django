from django.shortcuts import redirect, render

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
    
    queryset = Food.objects.all()


    return render(request, 'food.html', context={'food':queryset})


def delete_food(request, id):
    queyset = Food.objects.get(id = id)
    queyset.delete()
    return redirect('/')