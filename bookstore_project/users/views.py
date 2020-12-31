from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# SignupPageView references the
# CustomUserCreationForm, has a success_url that points to the login page meaning after
# the form is submitted the user will be redirected there