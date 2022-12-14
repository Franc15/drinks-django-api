from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view

api_view(['GET', 'POST'])
def drink_list(request):

    if request.method == 'GET':
        # get all the drinks
        drinks = Drink.objects.all()
        # serialize the data
        serializer = DrinkSerializer(drinks, many=True)
        # return the serialized data as json
        return JsonResponse({'drinks' : serializer.data})
