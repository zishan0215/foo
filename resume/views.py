from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, FormView
from django.contrib import messages
from .forms import FilebabyForm

# Create your views here.
class FileAddView(FormView):

    form_class = FilebabyForm
    success_url = reverse_lazy('resume-add')
    template_name = "resume/add.html"

    def form_valid(self, form):
        form.save(commit=True)
        messages.success(self.request, 'File uploaded!')
        return super(FileAddView, self).form_valid(form)