from django.contrib import admin

# Register your models here.

from .models import Jogador, Clube, Categoria, PosicaoSetor, Posicao, Busca, Conexao

@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ('nome','data_nascimento', 'imagem', 'email', 'telefone')

@admin.register(Clube)
class ClubeAdmin(admin.ModelAdmin):
    list_display = ('nome','descricao', 'imagem')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(PosicaoSetor)
class PosicaoSetorAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Posicao)
class PosicaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'setor')

@admin.register(Busca)
class BuscaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'clube', 'posicao', 'categoria')

@admin.register(Conexao)
class ConexaoAdmin(admin.ModelAdmin):
    list_display = ('clube', 'jogador')