from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password



User = get_user_model()
attrs = {'attrs': {'class': 'form-control'}}
email = forms.EmailInput(**attrs)
password = forms.PasswordInput(**attrs)




class RegisterModelForm(forms.ModelForm):

    # password = forms.CharField(label='Введите пароль', required=True, widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Введите пароль еще раз', required=True, widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = 'email', 'password', 'password2',

        widgets = {'email': email,
                   'password': password,
                   'password2': password,}

        labels = {'email': 'Введите email',
                  'password': 'Введите пароль',
                  'password2': 'Введите пароль еще раз',}

    def clean_password2(self, *args, **kwargs):
        data = self.cleaned_data
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise forms.ValidationError('Пароли должны совпадать')
        else:
            return password2




class LoginForm(forms.Form):

    email = forms.CharField(label='email',required=True, widget=email)
    password = forms.CharField(label='password',required=True, widget=password)

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        email = data.get('email')
        password = data.get('password')
        user_exists = User.objects.filter(email=email).first()

        if not user_exists:
            raise forms.ValidationError('Такого пользователя не существует')
        if not check_password(password, user_exists.password):
            raise forms.ValidationError('Пароль не верный')
        user = authenticate(email=email, password=password)
        if not user:
            raise forms.ValidationError('Данный аккаунт отключен')

        super(LoginForm, self).clean(*args, **kwargs)


