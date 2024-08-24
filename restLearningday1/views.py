from django.http import JsonResponse
from .models import Drink
from .serializers import Drinkserializer

def Home(request):
    drinks = Drink.objects.all()
    serializers = Drinkserializer(drinks, many=True)
    return JsonResponse(serializers.data, safe=False)


