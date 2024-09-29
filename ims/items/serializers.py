from rest_framework import serializers
from .models import Post


class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
    
    def update(self, instance, data):
        instance.name=data.get('name', instance.name)
        instance.description=data.get('description', instance.description)
        instance.quantity=data.get('quantity', instance.quantity)  
        instance.save ()
        return instance