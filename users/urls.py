from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from users.apps import UsersConfig
from users.views import *

app_name = UsersConfig.name


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/list/', UserListView.as_view(), name='users_list'),
    path('users/create/', UserCreateView.as_view(), name='users_create'),
    path('users/detail/<int:pk>', UserRetrieveView.as_view(), name='users_detail'),
    path('users/update/<int:pk>', UserUpdateView.as_view(), name='users_update'),
    path('users/delete/<int:pk>', UserDestroyView.as_view(), name='users_delete')
]