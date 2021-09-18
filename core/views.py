from django.views.generic import TemplateView,CreateView
from core import models
from core import forms
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['depoimentos'] = models.Depoimentos.objects.all()
        context['redes_sociais'] = models.Redes_Sociais.objects.all()
        return context

class ArticleView(TemplateView):
    template_name = 'article.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['redes_sociais'] = models.Redes_Sociais.objects.all()
        return context

class PrivacyView(TemplateView):
    template_name = 'privacy.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['redes_sociais'] = models.Redes_Sociais.objects.all()
        return context

class TermsView(TemplateView):
    template_name = 'terms.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['redes_sociais'] = models.Redes_Sociais.objects.all()
        return context

class SignupView(CreateView):
    template_name = 'sign-up.html'
    form_class = forms.SignupForm
    success_url = reverse_lazy('index')

class LoginView(LoginView):
    template_name = 'log-in.html'
