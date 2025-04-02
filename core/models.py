from django.db import models
from stdimage.models import StdImageField
import uuid

def get_file_path(_instance, filename):
    extensao = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{extensao}'
    return filename

#gera nome de arquivo aleatorio a fim de nao ter iamegns com msm nome 'db13bbf6-b40d-417f-ac3c-d26e5ac318ca'

class Base(models.Model):
    criados = models.DateField('criação',auto_now_add=True)         # auto_now_add=True: Preenche com a data/hora na criação do registro.
    modificado = models.DateField('atualização', auto_now=True)     # auto_now=True: Atualiza sempre que o registro for modificado.
    ativo = models.BooleanField('Ativo?',default=True)              # registro está ativo ou não. default=True: valor padrão será ativo

    class Meta:
        abstract = True

class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('icone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'serviço'
        verbose_name_plural = 'serviços'

    def __str__(self):
        return self.servico
        

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo
    
class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey("core.Cargo", verbose_name=('Cargo'), on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': { 'width': 480, 'height': 480, 'crop': True }}) 
    facebook = models.CharField('Facebook', max_length=100,default='#')
    twitter = models.CharField('Twitter',max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome
    
class Recurso(Base):
    ICONE_CHOICES = (
        ('lni-laptop-phone', 'Notebook'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )

    nome = models.CharField('Nome',max_length=100)
    icone = models.CharField('ícone',max_length=20,choices=ICONE_CHOICES)
    descricao = models.TextField('Descrição', max_length=200)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.nome