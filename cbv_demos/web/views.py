from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView, DeleteView

from cbv_demos.web.models import Article


class ArticleView(ListView):
    template_name = 'test.html'
    model = Article
    context_object_name = 'article'
    paginate_by = 5


class ArticleDetail(DetailView):
    template_name = 'detail.html'
    model = Article


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')
        widgets = {'title': forms.TextInput,
                   'content': forms.Textarea,
                   }


class ArticleCreate(CreateView):
    template_name = 'create.html'
    model = Article
    form_class = ArticleCreateForm
    success_url = reverse_lazy('article')


class ArticleDeleteForm(forms.Form):
    title = forms.CharField(max_length=30)


class ArticleDelete(DeleteView):
    model = Article
    template_name = 'delete.html'
    success_url = reverse_lazy('article')
