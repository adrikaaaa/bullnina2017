# coding: utf8
from django.db import models
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from utils import generate_image_filename

REGIOES = (
	('', u'SELECIONE A REGIÃO ONDE MORA'),
    (u'ZONA NORTE', u'ZONA NORTE'),
    (u'ZONA SUL', u'ZONA SUL'),
    (u'ZONA LESTE', u'ZONA LESTE'),
    (u'ZONA OESTE', u'ZONA OESTE'),
    (u'OUTRA CIDADE', u'OUTRA CIDADE'),
)

RACAS = (
	('', u'SELECIONE A RAÇA DO ANIMAL'),
	(u'BULDOGUE INGLÊS', u'BULDOGUE INGLÊS'),
    (u'BULDOGUE FRANCÊS', u'BULDOGUE FRANCÊS'),
    (u'GOLDEN RETRIEVER', u'GOLDEN RETRIEVER'),
    (u'SPITZ ALEMÃO', u'SPITZ ALEMÃO'),
    (u'LABRADOR', u'LABRADOR'),
    (u'PUG', u'PUG'),
    (u'VIRA LATA', u'VIRA LATA'),
    (u'MALTÊS', u'MALTÊS'),
    (u'YORKSHIRE', u'YORKSHIRE'),
    (u'BOXER', u'BOXER'),
    (u'PASTOR', u'PASTOR'),
    (u'LHASA APSO', u'LHASA APSO'),
    (u'OUTROS', u'OUTROS'),
)

IDADES = (
	('', u'SELECIONE A IDADE DO ANIMAL'),
	(u'ATÉ 1 ANO', u'ATÉ 1 ANO'),
	(u'2 ANOS', u'2 ANOS'),
	(u'3 ANOS', u'3 ANOS'),
	(u'4 ANOS', u'4 ANOS'),
	(u'5 ANOS', u'5 ANOS'),
	(u'6 ANOS', u'6 ANOS'),
	(u'7 ANOS', u'7 ANOS'),
	(u'8 ANOS', u'8 ANOS'),
	(u'9 ANOS', u'9 ANOS'),
	(u'10 ANOS', u'10 ANOS'),
	(u'11 ANOS', u'11 ANOS'),
	(u'12 ANOS', u'12 ANOS'),
	(u'13 ANOS', u'13 ANOS'),
	(u'14 ANOS', u'14 ANOS'),
	(u'15 ANOS', u'15 ANOS'),
	(u'16 ANOS', u'16 ANOS'),
	(u'17 ANOS', u'17 ANOS'),
	(u'18 ANOS', u'18 ANOS'),
	(u'19 ANOS', u'19 ANOS'),
	(u'20 ANOS', u'20 ANOS'),
	(u'MAIS DE 20 ANOS', u'MAIS DE 20 ANOS'),
)

RAMO = (
	('', u'SELECIONE O RAMO DE ATUAÇÃO'),
	(u'ALIMENTAÇÃO', u'ALIMENTAÇÃO'),
	(u'ACESSÓRIOS', u'ACESSÓRIOS'),
	(u'BRINQUEDOS', u'BRINQUEDOS'),
	(u'ROUPAS', u'ROUPAS'),
	(u'DECORAÇÃO', u'DECORAÇÃO'),
	(u'OUTROS', u'OUTROS'),
)


class Inscricao(models.Model):
	proprietario = models.CharField(max_length=120,
									verbose_name=u"Nome do proprietário")
	email = models.EmailField(verbose_name="email")
	telefone = models.CharField(max_length=15,
							    verbose_name=u"Telefone")
	regiao = models.CharField(choices=REGIOES, max_length=20,
							  verbose_name=u"Região onde mora")
	data_criacao = models.DateTimeField(
	        default=timezone.now)
	ativo = models.BooleanField(
			default=True)


class Cachorro(models.Model):
	inscricao = models.ForeignKey(Inscricao,
	    						  on_delete=models.CASCADE,
	)
	nome = models.CharField(max_length=120,
							verbose_name=u"Nome do cachorro")
	raca = models.CharField(choices=RACAS, max_length=20,
							verbose_name=u"Raça")
	idade = models.CharField(choices=IDADES, max_length=20,
							 verbose_name=u"Idade do cachorro")
	foto = ProcessedImageField(upload_to=generate_image_filename, blank=False,
                                processors=[ResizeToFill(300, 300)],
                                format='JPEG',
                                options={'quality': 100},
                                null=False)
	vacinado = models.BooleanField(
			default=False,
			verbose_name=u"Vacinado?")
	vermifugado = models.BooleanField(
			default=False,
			verbose_name=u"Vermifugado?")


class Expositor(models.Model):
	nome_marca = models.CharField(max_length=120,
								  verbose_name=u"Nome da marca")
	proprietario = models.CharField(max_length=120,
									verbose_name=u"Nome do proprietário")
	email = models.EmailField(verbose_name=u"Email")
	telefone = models.CharField(max_length=15,
								verbose_name=u"Telefone")
	ramo = models.CharField(choices=RAMO, max_length=20,
							verbose_name=u"Ramo da marca")
	descricao = models.TextField(max_length=200,
								 verbose_name=u"Breve descrição")
	foto = ProcessedImageField(upload_to=generate_image_filename, blank=False,
                                processors=[ResizeToFill(600, 400)],
                                format='JPEG',
                                options={'quality': 100},
                                null=False)
	data_criacao = models.DateTimeField(
	        default=timezone.now)
	ativo = models.BooleanField(
			default=False)


class Patrocinador(models.Model):
	nome_empresa = models.CharField(max_length=120, 
									verbose_name=u"Nome da empresa")
	nome_responsavel = models.CharField(max_length=120,
										verbose_name=u"Nome do responsável")
	email = models.EmailField(verbose_name=u"Email")
	telefone = models.CharField(max_length=15,
								verbose_name=u"Telefone")
	data_criacao = models.DateTimeField(
	        default=timezone.now)
