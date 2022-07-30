from django.shortcuts import render, get_object_or_404
from .models import Grade
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )


# Create your views here.
@login_required
def index(request):
    context={
        'grades':Grade.objects.filter(student=request.user),
        'allGrades':Grade.objects.all()
    }
    return render(request,'grades/grades.html',context)

class GradeDetailView(LoginRequiredMixin,DetailView):
    model=Grade


class GradeCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model=Grade
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
    success_url='/grades/'
    def test_func(self):
        if self.request.user.email[0:4]=='prof' or self.request.user.is_superuser:
            return True
        return False
    