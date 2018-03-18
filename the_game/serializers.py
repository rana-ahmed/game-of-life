from rest_framework import serializers
from .models import TheGame


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheGame
        fields = '__all__'
