#! /usr/bin/env python2.7
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

        
        expositores = Expositor.objects.filter(ativo=True).all()

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

        context = {}
        context['form_inscricao'] = form_inscricao
        context['form_expositores'] = ExpositorForm()
        context['form_patrocinadores'] = PatrocinadorForm()
        context['cachorro_form'] = formset
        
        return self.render_to_response(context)


class FormExpositoresView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        
        context = {}
        context['form_inscricao'] = InscricaoForm()
        context['form_expositores'] = ExpositorForm()
        context['form_patrocinadores'] = PatrocinadorForm()
        
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form_expositor = ExpositorForm(request.POST, 
        							   request.FILES)
        if form_expositor.is_valid():
        	form_expositor.save()
        	request.session['save_form'] = "expo"
        	return HttpResponseRedirect('/#eight')

        context = {}    
        context['form_inscricao'] = InscricaoForm()
        context['form_expositores'] = form_expositor
        context['form_patrocinadores'] = PatrocinadorForm()
        
        return self.render_to_response(context)


class FormPatrocinadoresView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        
        context = {}
        context['form_inscricao'] = InscricaoForm()
        context['form_expositores'] = ExpositorForm()
        context['form_patrocinadores'] = PatrocinadorForm()
        
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form_patrocinador = PatrocinadorForm(request.POST)
        if form_patrocinador.is_valid():
        	form_patrocinador.save()
        	request.session['save_form'] = "patro"
        	return HttpResponseRedirect('/#ten')

        context = {}	
       	context['form_inscricao'] = InscricaoForm()
        context['form_expositores'] = ExpositorForm()
        context['form_patrocinadores'] = form_patrocinador
        
        return self.render_to_response(context)


class HalloweenView(TemplateView):
    template_name = 'bulldogada2016.html'

    def get(self, request, *args, **kwargs):
        
        context = {}
        
        inscritos = Cachorro.objects.all()

        context['inscritos'] = inscritos
        return self.render_to_response(context)
