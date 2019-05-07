from django.urls import path

from .views import SocialAuthView, UserView

urlpatterns = [
    path('social/<str:backend>/', SocialAuthView.as_view(), name='login'),
    path('user', UserView.as_view(), name='user'),


]
