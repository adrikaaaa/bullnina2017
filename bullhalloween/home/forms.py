from django import forms
from django.forms.models import inlineformset_factory

from models import (Inscricao,
					Cachorro,
					Expositor,
					Patrocinador)


class InscricaoForm(forms.ModelForm):

    class Meta:
        model = Inscricao
        fields = ('proprietario', 'email', 'telefone', 'regiao')
        exclude = ('data_criacao', 'ativo')

        widgets = {
            'proprietario' : forms.TextInput(attrs = {
                'placeholder': u'Nome do proprietario'}),
            'email'    : forms.TextInput(attrs = {
                'placeholder': u'E-Mail'}),
            'telefone'    : forms.TextInput(attrs = {
                'placeholder': u'Telefone', 'class':'mask-phone'}),
        }

    def __init__(self, *args, **kwargs):
        super(InscricaoForm, self).__init__(*args, **kwargs)

        my_default_errors = {
            'required': u'Campo obrigatorio',
            'invalid': u'Campo invalido'
        }

        for k, field in self.fields.items():
            field.error_messages = my_default_errors


class CachorroForm(forms.ModelForm):

    class Meta:
        model = Cachorro
        fields = ('nome',
        		  'raca',
        		  'idade',
        		  'foto',
        		  'vacinado',
        		  'vermifugado')
        exclude = ('inscricao', )

        widgets = {
            'nome' : forms.TextInput(attrs = {
                'placeholder': u'Nome do cachorro'}),
        }

    def __init__(self, inscricao=None, *args, **kwargs):
        super(CachorroForm, self).__init__(*args, **kwargs)
        if inscricao:
            self.inscricao = inscricao

        my_default_errors = {
            'required': u'Campo obrigatorio',
            'invalid': u'Campo invalido'
        }

        for k, field in self.fields.items():
            field.error_messages = my_default_errors


CachorroFormset = inlineformset_factory(Inscricao, Cachorro, form=CachorroForm, extra=5)


class ExpositorForm(forms.ModelForm):

    class Meta:
        model = Expositor
        fields = ('nome_marca',
        		  'proprietario',
        		  'email',
        		  'telefone',
        		  'ramo',
        		  'descricao',
        		  'foto')
        exclude = ('data_criacao', 'ativo')

        widgets = {
            'nome_marca' : forms.TextInput(attrs = {
                'placeholder': u'Nome da marca'}),
            'proprietario' : forms.TextInput(attrs = {
                'placeholder': u'Nome do proprietario'}),
            'email' : forms.TextInput(attrs = {
                'placeholder': u'E-Mail'}),
            'telefone'    : forms.TextInput(attrs = {
                'placeholder': u'Telefone', 'class':'mask-phone'}),
            'descricao'    : forms.TextInput(attrs = {
                'placeholder': u'Breve descricao sobre a marca'}),
        }

    def __init__(self, *args, **kwargs):
        super(ExpositorForm, self).__init__(*args, **kwargs)

        my_default_errors = {
            'required': u'Campo obrigatorio',
            'invalid': u'Campo invalido'
        }

        for k, field in self.fields.items():
            field.error_messages = my_default_errors




class PatrocinadorForm(forms.ModelForm):

    class Meta:
        model = Patrocinador
        fields = ('nome_empresa', 'nome_responsavel', 'telefone', 'email')
        exclude = ('data_criacao',)

        widgets = {
            'nome_empresa' : forms.TextInput(attrs = {
                'placeholder': u'Nome da empresa'}),
            'nome_responsavel' : forms.TextInput(attrs = {
                'placeholder': u'Nome do responsavel'}),
            'email' : forms.TextInput(attrs = {
                'placeholder': u'E-Mail'}),
            'telefone': forms.TextInput(attrs = {
                'placeholder': u'Telefone', 'class':'mask-phone'}),
        }


    def __init__(self, *args, **kwargs):
        super(PatrocinadorForm, self).__init__(*args, **kwargs)

        my_default_errors = {
            'required': u'Campo obrigatorio',
            'invalid': u'Campo invalido'
        }

        for k, field in self.fields.items():
            field.error_messages = my_default_errors
 



