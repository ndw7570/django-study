from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)) # ViewSet URL 라우터 구성, ''은 상위 경로(/api)를 의미함: ViewSet은 기본적인 CRUD만 허용하므로 실무에서 사용하기엔 비추. 특히 중복 검사 등도 복잡해질 수 있으므로 그냥 APIVeiw 사용하는 것이 좋다고 생각한다.
]

