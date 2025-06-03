from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

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
