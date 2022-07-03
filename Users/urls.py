from django.urls import path
from Users import views

urlpatterns=[
    path("account/signup",views.SignUpView.as_view(),name="signup"),
    path("account/signin", views.SignInView.as_view(), name="signin")

]
