from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView
from employer.models import Jobs
from candidate.models import CandidateProfileModel
from candidate.forms import CandidateProfileForm

# Create your views here.

class CandidateTemplateView(TemplateView):
    template_name = "candi-home.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        qs=Jobs.objects.all()
        context["jobs"]=qs
        return context


class CandidateProfileCreateView(CreateView):
    model = CandidateProfileModel
    form_class = CandidateProfileForm
    template_name = "profile.html"
    success_url = reverse_lazy("candi-home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
