import uuid #gera valores hexadecimais aleatórios

from django.db import models
from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    # Ex.: 'teste.png', com o split ('.') teremos 2 partes e com -1 pegaremos a última parte.
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now_add=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Jogador(Base):
    nome = models.CharField('Nome', max_length=100)
    data_nascimento = models.DateField('Data de Nascimento')
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    descricao = models.TextField('Descrição', max_length=500, default="")
    email = models.CharField('Email', max_length=150, default="")
    telefone = models.CharField('Telefone', max_length=20, default="")

    class Meta:
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogador'

    def __str__(self):
        return self.nome


class Clube(Base):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', max_length=500)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 350, 'height': 350, 'crop': True}})
    cor = models.CharField('Cor', max_length=10, default='#fff')

    class Meta:
        verbose_name = 'Clube'
        verbose_name_plural = 'Clubes'

    def __str__(self):
        return self.nome


class Categoria(Base):
    nome = models.CharField('Nome', max_length=200)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome


class PosicaoSetor(Base):
    nome = models.CharField('Nome', max_length=200)

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'

    def __str__(self):
        return self.nome

class Posicao(Base):
    nome = models.CharField('Nome', max_length=200)
    setor = models.ForeignKey('busca.PosicaoSetor', verbose_name='Setor', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Posição'
        verbose_name_plural = 'Posições'

    def __str__(self):
        return self.nome


class Busca(Base):
    descricao = models.TextField('Descrição', max_length=1000)
    clube = models.ForeignKey('busca.Clube', verbose_name='Clube', on_delete=models.CASCADE)
    posicao = models.ForeignKey('busca.Posicao', verbose_name='Posição', on_delete=models.CASCADE)
    categoria = models.ForeignKey('busca.Categoria', verbose_name='Categoria', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Busca'
        verbose_name_plural = 'Buscas'

    def __str__(self):
        return self.descricao


class Conexao(Base):
    clube = models.ForeignKey('busca.Clube', verbose_name='Clube', on_delete=models.CASCADE)
    jogador = models.ForeignKey('busca.Jogador', verbose_name='Jogador', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Conexão'
        verbose_name_plural = 'Conexão'

    def __str__(self):
        return self.clube

