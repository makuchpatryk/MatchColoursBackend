from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
      path('user/', views.UserDetail.as_view()),
      path("auth/login/google/", views.GoogleLoginApi.as_view(), 
         name="login-with-google"),
      path("auth/login/github/", views.GithubLoginApi.as_view(), 
         name="login-with-github"),
      path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
      path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]