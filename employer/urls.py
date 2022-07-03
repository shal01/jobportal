from django.urls import path
from employer import views

urlpatterns =[
    path("emp",views.EmployeeHomeView.as_view(),name="e-home"),
    path("profile/add",views.EmployerProfileCreateView.as_view(),name="emp-profile"),
    path("profile/details",views.EmployeeProfileDetailView.as_view(),name="emp-datails"),
    path("jobs/add",views.JobCreateView.as_view(),name="addjob"),
    path("jobs/all",views.JobListView.as_view(),name="all-jobs"),
    path("jobs/detail/<int:id>",views.JobDetailView.as_view(),name="emp-jobdetial"),
    path("jobs/update/<int:id>",views.JobEditView.as_view(),name="job-edit"),
]