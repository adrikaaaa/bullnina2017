# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import bullhalloween.home.utils
import django.utils.timezone
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cachorro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=120, verbose_name='Nome do cachorro')),
                ('raca', models.CharField(max_length=20, verbose_name='Ra\xe7a', choices=[('BULDOGUE INGL\xcaS', 'BULDOGUE INGL\xcaS'), ('BULDOGUE FRANC\xcaS', 'BULDOGUE FRANC\xcaS'), ('GOLDEN RETRIEVER', 'GOLDEN RETRIEVER'), ('SPITZ ALEM\xc3O', 'SPITZ ALEM\xc3O'), ('LABRADOR', 'LABRADOR'), ('PUG', 'PUG'), ('VIRA LATA', 'VIRA LATA'), ('MALT\xcaS', 'MALT\xcaS'), ('YORKSHIRE', 'YORKSHIRE'), ('BOXER', 'BOXER'), ('PASTOR', 'PASTOR'), ('LHASA APSO', 'LHASA APSO'), ('OUTROS', 'OUTROS')])),
                ('idade', models.CharField(max_length=20, verbose_name='Idade do cachorro', choices=[('AT\xc9 1 ANO', 'AT\xc9 1 ANO'), ('2 ANOS', '2 ANOS'), ('3 ANOS', '3 ANOS'), ('4 ANOS', '4 ANOS'), ('5 ANOS', '5 ANOS'), ('6 ANOS', '6 ANOS'), ('7 ANOS', '7 ANOS'), ('8 ANOS', '8 ANOS'), ('9 ANOS', '9 ANOS'), ('10 ANOS', '10 ANOS'), ('11 ANOS', '11 ANOS'), ('12 ANOS', '12 ANOS'), ('13 ANOS', '13 ANOS'), ('14 ANOS', '14 ANOS'), ('15 ANOS', '15 ANOS'), ('16 ANOS', '16 ANOS'), ('17 ANOS', '17 ANOS'), ('18 ANOS', '18 ANOS'), ('19 ANOS', '19 ANOS'), ('20 ANOS', '20 ANOS'), ('MAIS DE 20 ANOS', 'MAIS DE 20 ANOS')])),
                ('foto', imagekit.models.fields.ProcessedImageField(upload_to=bullhalloween.home.utils.generate_image_filename)),
                ('vacinado', models.BooleanField(default=True, verbose_name='Vacinado?')),
                ('vermifugado', models.BooleanField(default=True, verbose_name='Vermifugado?')),
            ],
        ),
        migrations.CreateModel(
            name='Expositor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_marca', models.CharField(max_length=120, verbose_name='Nome da marca')),
                ('proprietario', models.CharField(max_length=120, verbose_name='Nome do propriet\xe1rio')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('ramo', models.CharField(max_length=20, verbose_name='Ramo da marca', choices=[('ALIMENTA\xc7\xc3O', 'ALIMENTA\xc7\xc3O'), ('ACESS\xd3RIOS', 'ACESS\xd3RIOS'), ('BRINQUEDOS', 'BRINQUEDOS'), ('ROUPAS', 'ROUPAS'), ('DECORA\xc7\xc3O', 'DECORA\xc7\xc3O'), ('OUTROS', 'OUTROS')])),
                ('descricao', models.CharField(max_length=200, verbose_name='Breve descri\xe7\xe3o')),
                ('foto', imagekit.models.fields.ProcessedImageField(upload_to=bullhalloween.home.utils.generate_image_filename)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('ativo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('proprietario', models.CharField(max_length=120, verbose_name='Nome do propriet\xe1rio')),
                ('email', models.EmailField(max_length=254, verbose_name=b'email')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('regiao', models.CharField(max_length=20, verbose_name='Regi\xe3o onde mora', choices=[('ZONA NORTE', 'ZONA NORTE'), ('ZONA SUL', 'ZONA SUL'), ('ZONA LESTE', 'ZONA LESTE'), ('ZONA OESTE', 'ZONA OESTE'), ('OUTRA CIDADE', 'OUTRA CIDADE')])),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patrocinador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_empresa', models.CharField(max_length=120, verbose_name='Nome da empresa')),
                ('nome_responsavel', models.CharField(max_length=120, verbose_name='Nome do respons\xe1vel')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='cachorro',
            name='inscricao',
            field=models.ForeignKey(to='home.Inscricao'),
        ),
    ]
