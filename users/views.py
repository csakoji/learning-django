from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/sign_up.html'
    success_url = reverse_lazy('home')
