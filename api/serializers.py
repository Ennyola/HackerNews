from rest_framework import serializers
from news.models import Item

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        
