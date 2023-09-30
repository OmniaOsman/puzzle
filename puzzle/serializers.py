from rest_framework import serializers
from .models import Puzzle

class GetPuzzleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puzzle
        fields = '__all__'
        
        
class PostPuzzleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puzzle
        fields = ('data', 'level')
        
        