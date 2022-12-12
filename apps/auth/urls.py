from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path

from .views import ActivateUserView, ChangePasswordView, ResetPasswordView

urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('/refresh', TokenRefreshView.as_view()),
    path('/activate/<str:token>', ActivateUserView.as_view()),
    path('/reset_password', ResetPasswordView.as_view()),
    path('/change_password/<str:token>', ChangePasswordView.as_view())
]
