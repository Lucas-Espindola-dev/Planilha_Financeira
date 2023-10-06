from django.contrib import admin
from planilha.models import Receita, Despesa


class Receitas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data',)
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao',)
    ordering = ('descricao', )


admin.site.register(Receita, Receitas)


class Despesas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'categoria', 'valor', 'data')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao',)
    ordering = ('descricao', )


admin.site.register(Despesa, Despesas)

