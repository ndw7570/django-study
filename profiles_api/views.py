from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

# Django REST framework (DRF)
class HelloApiView(APIView): # APIView는 Django의 RESTful API를 만들기 쉽게 도와주는, JSON 형식의 응답을 주는 API 뷰 (HTML을 보여주는 뷰가 아니라)
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None): # format=None(DRF)은 Accept 헤더나 .json, .api 같은 URL 확장자를 통해 응답 포맷을 자동으로 처리
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview}) # Response({...})  → JSONRenderer로 JSON 직렬화 → HttpResponse 객체 생성 → WSGI를 통해 HTTP 프로토콜로 전송
    
    def post(self, request): # 함수 내에서 self 변수(serializer_class)를 사용하지 않아도 되지만, 정의는 반드시 있어야 함.
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data) #

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None): # 전체 리소스 교체(name, description, price)
        """Handle updating an object""" # doc string: 함수, 클래스, 모듈의 첫 줄로 런타임시 접근 가능
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None): # 일부 필드만 수정( price : 150 )
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def unpdate(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, ) # unique 해야 함으로 튜플 사용 # => Authentication
    permission_classes = (permissions.UpdateOwnProfile, ) # => Authorization