from django.urls import path
from candidate import views

urlpatterns=[
    path("home",views.CandidateTemplateView.as_view(),name="cand-home"),
    path("profile/add",views.CandidateProfileCreateView.as_view(),name="cand-addpro")
]