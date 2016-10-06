#! /usr/bin/env python2.7
import re
from django.views.generic import TemplateView
from forms import (InscricaoForm,
				   CachorroForm,
				   ExpositorForm,
				   PatrocinadorForm,
                   CachorroFormset)
from models import Inscricao, Expositor, Cachorro
from django.http import HttpResponseRedirect

from django.forms.models import inlineformset_factory


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        
        context = {}
    	if request.session.get('save_form'):
        	context['form_saved'] = request.session.get('save_form')
    		request.session.flush()

        expositores = []
        objs = Expositor.objects.filter(ativo=True).all()
        for expo in objs:
            expositores.append({
                'nome_marca': expo.nome_marca,
                'descricao': expo.descricao,
                'foto': expo.foto.build_url(
                    width=600,
                    height=400,
                    crop='fill')
                })

        context['numero_inscricao'] = Inscricao.objects.count()    
        context['form_inscricao'] = InscricaoForm()
        context['form_expositores'] = ExpositorForm()
        context['form_patrocinadores'] = PatrocinadorForm()
        context['cachorro_form'] = CachorroFormset(instance=Inscricao())
        context['expositores'] = expositores
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form_inscricao = InscricaoForm(request.POST)
        
        formset = CachorroFormset(request.POST,
                request.FILES,
                instance=Inscricao())    

        if form_inscricao.is_valid():

            inscricao = form_inscricao.save(commit=False)
            formset = CachorroFormset(request.POST,
                request.FILES,
                instance=inscricao)

            if formset.is_valid():
                form_inscricao.save(commit=True)
                formset.save() 
            
                request.session['save_form'] = "subs"
                return HttpResponseRedirect('/#six') 

        expositores = []
        objs = Expositor.objects.filter(ativo=True).all()
        for expo in objs:
            expositores.append({
                'nome_marca': expo.nome_marca,
                'descricao': expo.descricao,
                'foto': expo.foto.build_url(
                    width=600,
                    height=400,
                    crop='fill')
                })

        context = {}
        
        context['numero_inscricao'] = Inscricao.objects.count()   
        
        context['form_inscricao'] = form_inscricao
        context['form_expositores'] = ExpositorForm()
        context['form_patrocinadores'] = PatrocinadorForm()
        context['cachorro_form'] = formset
        context['expositores'] = expositores
        context['numero_inscricao'] = Inscricao.objects.count()
        
        return self.render_to_response(context)


class FormExpositoresView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

        expositores = []

        objs = Expositor.objects.filter(ativo=True).all()
        for expo in objs:
            expositores.append({
                'nome_marca': expo.nome_marca,
                'descricao': expo.descricao,
                'foto': expo.foto.build_url(
                    width=600,
                    height=400,
                    crop='fill')
                })

        context = {}
        
        context['numero_inscricao'] = Inscricao.objects.count()
        context['form_inscricao'] = InscricaoForm()
        context['form_expositores'] = ExpositorForm()
        context['form_patrocinadores'] = PatrocinadorForm()
        context['expositores'] = expositores
        context['numero_inscricao'] = Inscricao.objects.count()

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form_expositor = ExpositorForm(request.POST, 
        							   request.FILES)
        if form_expositor.is_valid():
        	form_expositor.save()
        	request.session['save_form'] = "expo"
        	return HttpResponseRedirect('/#eight')

        expositores = []

        objs = Expositor.objects.filter(ativo=True).all()
        for expo in objs:
            expositores.append({
                'nome_marca': expo.nome_marca,
                'descricao': expo.descricao,
                'foto': expo.foto.build_url(
                    width=600,
                    height=400,
                    crop='fill')
                })

        context = {}
        
        context['numero_inscricao'] = Inscricao.objects.count()  
        context['form_inscricao'] = InscricaoForm()
        context['form_expositores'] = form_expositor
        context['form_patrocinadores'] = PatrocinadorForm()
        context['expositores'] = expositores
        context['numero_inscricao'] = Inscricao.objects.count()

        return self.render_to_response(context)


class FormPatrocinadoresView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

        expositores = []
        
        objs = Expositor.objects.filter(ativo=True).all()
        for expo in objs:
            expositores.append({
                'nome_marca': expo.nome_marca,
                'descricao': expo.descricao,
                'foto': expo.foto.build_url(
                    width=600,
                    height=400,
                    crop='fill')
                })

        context = {}
        
        context['numero_inscricao'] = Inscricao.objects.count()
        context['form_inscricao'] = InscricaoForm()
        context['form_expositores'] = ExpositorForm()
        context['form_patrocinadores'] = PatrocinadorForm()
        context['expositores'] = expositores
        context['numero_inscricao'] = Inscricao.objects.count()

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form_patrocinador = PatrocinadorForm(request.POST)
        if form_patrocinador.is_valid():
        	form_patrocinador.save()
        	request.session['save_form'] = "patro"
        	return HttpResponseRedirect('/#ten')

        expositores = []    

        objs = Expositor.objects.filter(ativo=True).all()
        for expo in objs:
            expositores.append({
                'nome_marca': expo.nome_marca,
                'descricao': expo.descricao,
                'foto': expo.foto.build_url(
                    width=600,
                    height=400,
                    crop='fill')
                })

        context = {}
        
        context['numero_inscricao'] = Inscricao.objects.count()	
       	context['form_inscricao'] = InscricaoForm()
        context['form_expositores'] = ExpositorForm()
        context['form_patrocinadores'] = form_patrocinador
        context['expositores'] = expositores
        context['numero_inscricao'] = Inscricao.objects.count()

        return self.render_to_response(context)


class HalloweenView(TemplateView):
    template_name = 'bulldogada2016.html'

    def get(self, request, *args, **kwargs):

        context = {}
        inscritos = []
        objs = Cachorro.objects.order_by('?').all()
        for dog in objs:
            splited_name = str(dog.inscricao.proprietario).split(' ')
            image = str(dog.foto.build_url(
                    width=300,
                    height=300,
                    crop='fill'))
            final_image_name = re.sub(r'w_300/[^/]+','w_300', image)
            try:
                final_name = "{0} {1}".format(splited_name[0],
                                              splited_name[-1])
            except Exception:

                final_name = dog.inscricao.proprietario    
            inscritos.append({
                'nome': unicode(dog.nome),
                'prop': unicode(final_name),
                'foto': final_image_name,
                })

        context['inscritos'] = inscritos
        return self.render_to_response(context)
