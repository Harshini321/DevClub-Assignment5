
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import Announcement
from django.contrib.auth.models import User

# Create your views here.


class AnnListView(LoginRequiredMixin,ListView):
    model=Announcement
    template_name='communication/announcements.html'
    context_object_name='announcements'
    ordering=['-date_posted']

class AnnDetailView(LoginRequiredMixin,DetailView):
    model=Announcement
    context_object_name='announcement'

class AnnCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model=Announcement
    context_object_name='announcement'
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.email[0:4]=='prof' or self.request.user.is_superuser:
            return True
        return False

class AnnUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Announcement
    context_object_name='announcement'
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        announcement=self.get_object()
        if self.request.user==announcement.author or self.request.user.is_superuser:
            if self.request.user.email[0:4]=='prof' or self.request.user.is_superuser:
                return True
        return False

class AnnDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Announcement
    context_object_name='announcement'
    success_url='/announcements/'
    def test_func(self):
        announcement=self.get_object()
        if self.request.user==announcement.author or self.request.user.is_superuser:
            if self.request.user.email[0:4]=='prof' or self.request.user.is_superuser:
                return True
        return False
    
class UserAnnListView(LoginRequiredMixin,ListView):
    model=Announcement
    template_name='communication/user_announcements.html'
    context_object_name='announcements'
    
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        print(Announcement.objects.filter(author=user))
        return Announcement.objects.filter(author=user).order_by('-date_posted')

