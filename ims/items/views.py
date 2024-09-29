from django.shortcuts import render
from rest_framework. response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from .models import Post
from rest_framework.permissions import IsAuthenticated
from .serializers import postSerializer
import logging
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from django.conf import settings
CACHE_TTL = getattr (settings , 'CACHE_TTL' , DEFAULT_TIMEOUT)
logger = logging.getLogger("myapp.views") 

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def home(request):
    serializer = postSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'error': 'Item already exists'},status=status.HTTP_400_BAD_REQUEST)

@api_view( ['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def post(request,pk):
    Posts = cache.get(pk)
    if not Posts:
        try:
            Posts = Post.objects.get(pk=pk)
            cache.set(pk, Posts)
            
        except:
            logger.warning("object are not getting")
            return Response({'error': 'Item not found'},status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = postSerializer(Posts)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = postSerializer(Posts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        Posts.delete()
        return Response({'Response': 'Success'},status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_list (request):
    Posts = cache.get('all_Posts')
    print(Posts)
    if not Posts:
        Posts = Post.objects.all() 
        print("post from db")
        cache.set('all_Posts', Posts, 20)
    serializer = postSerializer(Posts, many=True)
    logger.info("All Values are getting")
    return Response(serializer.data)


