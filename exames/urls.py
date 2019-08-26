from django.urls import path
from exames.views import ExamesListView, ExamesCreateView, ExamesUpdateView, ExamesDeletView

app_name = "exames"

urlpatterns = [
    path('exames', ExamesListView.as_view(), name = 'ver_exames'),
    path('exames', ExamesCreateView.as_view(), name = 'criar_exames'),
    path('exames/<int:pk>/editar', ExamesUpdateView.as_view(), name = 'editar_exames'),
    path('exames/<int:pk>/deletar', ExamesDeletView.as_view(), name = 'deletar_exames'),
]
