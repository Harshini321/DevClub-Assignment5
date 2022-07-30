from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import Document
from django.contrib.auth.models import User

# Create your views here.

class DocListView(LoginRequiredMixin,ListView):
    model=Document
    template_name='documents/documents.html'
    context_object_name='documents'
    ordering=['-date_posted']

class DocDetailView(LoginRequiredMixin,DetailView):
    model=Document
    context_object_name='document'

class DocCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model=Document
    context_object_name='document'
    fields=['title','file']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.email[0:4]=='prof' or self.request.user.is_superuser:
            return True
        return False

class DocUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Document
    context_object_name='document'
    fields=['title','file']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        announcement=self.get_object()
        if self.request.user==announcement.author or self.request.user.is_superuser:
            if self.request.user.email[0:4]=='prof' or self.request.user.is_superuser:
                return True
        return False

class DocDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Document
    context_object_name='document'
    success_url='/documents/'
    def test_func(self):
        document=self.get_object()
        if self.request.user==document.author or self.request.user.is_superuser:
            if self.request.user.email[0:4]=='prof' or self.request.user.is_superuser:
                return True
        return False
    
class UserDocListView(LoginRequiredMixin,ListView):
    model=Document
    template_name='documents/user_documents.html'
    context_object_name='documents'
    
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Document.objects.filter(author=user).order_by('-date_posted')
