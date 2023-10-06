from django.db.models import Sum
from rest_framework import viewsets
from planilha.models import Receita, Despesa
from planilha.serializer import DespesaSerializer, ReceitaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response


class DespesaViewSet(viewsets.ModelViewSet):
    """Exibindo Despesas"""
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
    search_fields = ['descricao']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['descricao']


class DespesaMesAnoViewSet(viewsets.ModelViewSet):
    """Exibindo despesas por Mês/Ano"""
    serializer_class = DespesaSerializer

    def get_queryset(self):
        ano = self.kwargs['ano']
        mes = self.kwargs["mes"]
        return Despesa.objects.filter(data__year=ano, data__month=mes)


class ReceitaViewSet(viewsets.ModelViewSet):
    """Exibindo Receitas"""
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    search_fields = ['descricao', 'data__month' and 'data__year']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


class ReceitaMesAnoViewSet(viewsets.ModelViewSet):
    """Exibindo receitas por Mês/Ano"""
    serializer_class = ReceitaSerializer

    def get_queryset(self):
        ano = self.kwargs['ano']
        mes = self.kwargs['mes']
        return Receita.objects.filter(data__year=ano, data__month=mes)


class ResumoMesViewSet(APIView):
    """Balanço Receitas menos Despesas por Mês/Ano"""

    queryset = Receita.objects.none()

    def get(self, request, ano, mes):
        valor_total_receitas = not Receita.objects.filter(data__year=ano, data__month=mes).aggregate(
            Sum('valor'))['valor__sum'] or 0
        valor_total_despesas = not Despesa.objects.filter(data__year=ano, data__month=mes).aggregate(
            Sum('valor'))['valor__sum'] or 0
        despesa_por_categoria = Despesa.objects.filter(data__year=ano, data__month=mes).values(
            'categoria').annotate(Sum('valor'))
        saldo_final = valor_total_receitas - valor_total_despesas

        for i in despesa_por_categoria:
            i['valor'] = i['valor__sum']
            del i['valor__sum']

        return Response({
            'Receita/Mês': valor_total_receitas,
            'Despesa/Mês': despesa_por_categoria,
            'Categoria/Mês': despesa_por_categoria,
            'Saldo Final/Mês': saldo_final,
        })
