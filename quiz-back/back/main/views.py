from django.shortcuts import render
from main.models import Post
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from main.serializers import PostSerializer, LikeSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404


from django.http import Http404
# Create your views here.


class PostView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)

    def get_serializer_class(self):
        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class PostDetailView(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(id=pk)
        except Post.DoesNotExist as e:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)


class PostLike(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(id=pk)
        except Post.DoesNotExist as e:
            raise Http404

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = LikeSerializer(instance=post)
        if serializer.is_valid():
            post.like_count +=1
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST', ])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data.get('user')
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})


@api_view(['POST', ])
def logout(request):
    request.auth.delete()
    return Response(status=status.HTTP_200_OK)