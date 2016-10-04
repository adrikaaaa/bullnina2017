from datetime import datetime

from django import forms
from django.contrib import admin

from models import (
    Inscricao, Cachorro, Expositor, Patrocinador
)


class InscricaoAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(InscricaoAdminForm, self).__init__(*args, **kwargs)

    class Meta:
    	fields = ('proprietario', 'email', 'telefone', 'regiao', 'ativo')
        model = Inscricao
        

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('proprietario', 'email', 'telefone', 'regiao', 'data_criacao')
    form = InscricaoAdminForm

    def save_model(self, request, obj, form, change):
        obj.save()


class CachorroAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CachorroAdminForm, self).__init__(*args, **kwargs)

    class Meta:
    	fields = ('nome', 'raca', 'vacinado', 'vermifugado')
        model = Cachorro
        

@admin.register(Cachorro)
class CachorroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'raca', 'vacinado', 'vermifugado')
    form = CachorroAdminForm

    def save_model(self, request, obj, form, change):
        obj.save()


class ExpositoresAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ExpositoresAdminForm, self).__init__(*args, **kwargs)

    class Meta:
    	fields = ('nome_marca', 'proprietario', 'email', 'telefone', 'ramo', 'descricao', 'ativo', 'foto')
        model = Expositor
        

@admin.register(Expositor)
class ExpositorAdmin(admin.ModelAdmin):
    list_display = ('nome_marca', 'proprietario', 'email', 'telefone', 'ramo', 'ativo', 'data_criacao')
    form = ExpositoresAdminForm

    def save_model(self, request, obj, form, change):
        obj.save()


class PatrocinadoresAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PatrocinadoresAdminForm, self).__init__(*args, **kwargs)

    class Meta:
    	fields = ('nome_empresa', 'nome_responsavel', 'email', 'telefone', 'data_criacao')
        model = Patrocinador
        

@admin.register(Patrocinador)
class PatrocinadorAdmin(admin.ModelAdmin):
    list_display = ('nome_empresa', 'nome_responsavel', 'email', 'telefone', 'data_criacao')
    form = PatrocinadoresAdminForm

    def save_model(self, request, obj, form, change):
        obj.save()
