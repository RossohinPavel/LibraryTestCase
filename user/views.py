from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import RegisterUserForm, LoginUserForm


# Create your views here.
class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'user/logreg.html'
    extra_context = {
        'title': "Регистрация",
        'button_label': 'Зарегистрироваться'
        }
    success_url = reverse_lazy('login')


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'user/logreg.html'
    extra_context = {
        'title': "Авторизация",
        'button_label': 'Войти'
    }
    success_url = reverse_lazy('home')
