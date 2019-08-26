from django.urls import path
from users.views import UserLoginViews, UserLogoutView, UserCadastroView

app_name = 'users'

urlpatterns = [
    path('logar',UserLoginViews.as_view(),name = 'logar_user'),
    path('logout',UserLogoutView.as_view(),name = 'logout_user'),   
    path('cadastro',UserCadastroView.as_view(),name = 'cadastro_user'),
]

