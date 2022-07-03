from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView
from Users.forms import UserRegistrationForm,LoginForm
from Users.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login

class SignUpView(CreateView):
    model = User
    template_name = "register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("signin")

class SignInView(FormView):
    model=User
    form_class = LoginForm
    template_name ="Login.html"

    def post(self, request, *args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if not user:
                return render(request,'login.html',{"form":form})
            login(request,user)
            if request.user.is_candidate:
                return redirect("cand-home")
            else:
                return redirect("e-home")

