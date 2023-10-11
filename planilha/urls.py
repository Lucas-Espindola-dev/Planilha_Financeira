from planilha.views import *
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register('despesas', DespesaViewSet, basename='despesas')
router.register('receitas', ReceitaViewSet, basename='receitas')


urlpatterns = [
    path('', include(router.urls)),
    path('receitas/<int:mes>/<int:ano>', ReceitaMesAnoViewSet.as_view({'get': 'list'})),
    path('despesas/<int:mes>/<int:ano>', ReceitaMesAnoViewSet.as_view({'get': 'list'})),
    path('resumo/<int:mes>/<int:ano>', ResumoMesViewSet.as_view()),
    path('registro/', RegistraUsuarioView.as_view()),
]
