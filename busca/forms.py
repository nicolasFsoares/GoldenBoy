from django.forms import ModelForm
from busca.models import Jogador, Conexao

class JogadorForm(ModelForm):
     class Meta:
         model = Jogador
         fields = ['imagem', 'nome', 'descricao', 'email', 'telefone']



class ConexaoForm(ModelForm):
    class Meta:
        model = Conexao
        fields = ['clube', 'jogador']