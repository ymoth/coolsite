from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):
    """
    Создание новой формы для создания новой статьи
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    # Мета-класс для реализации интеграции отображения виджетов
    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        if not self.cleaned_data['username'].isascii() or self.cleaned_data['username'].isdigit():
            raise ValidationError('Ошибка авторизации, имя должно быть латинскими буквами')
        if User.objects.filter(username=self.cleaned_data['username']) is not None:
            raise ValidationError('Данный пользователь уже зарегистрирован.')

        # Return true data
        return self.cleaned_data['username']

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']) is not None:
            raise ValidationError('Пользователь уже зарегистрирован по данной почте.')
        return self.cleaned_data['email']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput())
    password = forms.CharField(label='Password', widget=forms.PasswordInput())


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email', )
    content = forms.CharField(label='Описание ', max_length=1000)
    capatcha = CaptchaField()
