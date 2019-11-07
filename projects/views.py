from django.shortcuts import render
from django.views.generic import (ListView,DetailView,
                                  CreateView,UpdateView,DeleteView)
from .models import Projects

# Create your views here.
class ProjectListView(ListView):
    model = Projects
    template_name = 'projects/projects.html'
    context_object_name = 'projects'
    ordering = ['-date_posted']
    paginate_by = 5


class ProjectDetailView(DetailView):
    model = Projects
