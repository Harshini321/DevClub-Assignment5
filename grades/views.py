from django.shortcuts import render

# Create your views here.
# def grade(request):
from django.shortcuts import render, get_object_or_404
from .models import Grade
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )


# Create your views here.

def index(request):
    context={
        'grades':Grade.objects.filter(student=request.user)
    }
    return render(request,'grades/grades.html',context)

class GradeDetailView(DetailView):
    model=Grade


class GradeCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model=Grade
    # context_object_name='announcement'
    fields=['course','marks','student']

    def test_func(self):
        if self.request.user.email[0:4]=='prof' or self.request.user.is_superuser:
            return True
        return False

class GradeUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Grade
    fields=['course','marks','student']
    def test_func(self):
        if self.request.user.email[0:4]=='prof' or self.request.user.is_superuser:
                return True
        return False

class GradeDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Grade
    # context_object_name='announcement'
    success_url='/grades/'
    def test_func(self):
        if self.request.user.email[0:4]=='prof' or self.request.user.is_superuser:
            return True
        return False
    