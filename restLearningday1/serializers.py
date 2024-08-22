from rest_framework import serializers
from .models import Drink

class Drinkserializer(serializers.ModelSerilizer):
    class Meta:
        model = Drink
        fields = ["id", "name", "description"]