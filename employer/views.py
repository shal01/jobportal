from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView
from employer.models import EmployeeProfile,Jobs
from employer.forms import EmployerProfileForm,JobForm,JobUpdateForm
# Create your views here.

class EmployeeHomeView(TemplateView):
    template_name = "emp_home.html"

class EmployerProfileCreateView(CreateView):
    model = EmployeeProfile
    form_class = EmployerProfileForm
    template_name = "emp-profile.html"
    success_url = reverse_lazy("e-home")

    # def post(self, request, *args, **kwargs):
    #     form=EmployerProfileForm(request.POST,files=request.FILES)
    #     if  form.is_valid():
    #         profile=form.save(commit=False)
    #         profile.user=request.user
    #         profile.save()
    #         print("Profile Created")
    #         return redirect("e-home")
    #     else:
    #         return render(request,self.template_name,{'form':form})


    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class EmployeeProfileDetailView(TemplateView):
    template_name = "emp_myprofile.html"


class JobCreateView(CreateView):
    model = Jobs
    form_class = JobForm
    template_name = "emp-postjob.html"
    success_url = reverse_lazy("e-home")

    def form_valid(self, form):
        form.instance.posted_by=self.request.user
        return super().form_valid(form)


class JobListView(ListView):
    model = Jobs
    context_object_name = "jobs"
    template_name = "emp-job-list.html"

    def get_queryset(self):
        return Jobs.objects.filter(posted_by=self.request.user)


class JobDetailView(DetailView):
    model = Jobs
    template_name = "emp-jobdetail.html"
    context_object_name = "job"
    pk_url_kwarg = "id"

class JobEditView(UpdateView):
    model = Jobs
    form_class = JobUpdateForm
    template_name = "emp-jobedit.html"
    success_url = reverse_lazy("all-jobs")
    pk_url_kwarg = "id"

