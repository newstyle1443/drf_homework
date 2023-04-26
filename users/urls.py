from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('list/', views.UserList.as_view(), name='user_list'),
    path("signin/", views.signin.as_view(), name='signin'),
    path('update/<int:user_id>/', views.UserUpdate.as_view(), name='user_update'),
    path('delete/<int:user_id>/', views.UserDelete.as_view(), name='user_delete'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]