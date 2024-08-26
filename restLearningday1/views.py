from django.http import JsonResponse
from .models import Drink
from .serializers import Drinkserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def Home(request):
    if request.method == "GET":
        drinks = Drink.objects.all()
        serializers = Drinkserializer(drinks, many=True)
        return JsonResponse({"Data":serializers.data})
    
    if request.method == "POST":
        serializers = Drinkserializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
