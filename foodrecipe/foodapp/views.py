from django.shortcuts import redirect, render

from foodapp.models import *




# Create your views here.
# for create food
def foodview(request):



    if request.method == "POST":
        data = request.POST
        image = request.FILES.get('image')
        name = data.get('name')
        description = data.get('description')

        Food.objects.create(
            food_image = image,
            food_name = name,
            food_description = description
        )
    
    queryset = Food.objects.all().order_by('id')
    
    return render(request, 'food.html', context={'food':queryset})

#for update food

def update_food(request, id):
    queryset = Food.objects.get(id = id)
    if request.method == "POST":
        data = request.POST

        image = request.FILES.get('food_image')
        name = data.get('food_name')
        description = data.get('food_description')

        queryset.food_name = name
        queryset.food_description = description
        queryset.food_image = image
        
        queryset.save()
        return redirect('/')

        
    return render(request, 'updatefood.html', context={'food':queryset})




#for delete food
def delete_food(request, id):
    Food.objects.get(id = id).delete()
    return redirect('/')


#views complete