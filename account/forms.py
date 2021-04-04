from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import ProfileUserModel


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'



class profile_form(forms.ModelForm):
    """Форма профиля"""

    class Meta:
        model = ProfileUserModel
        fields = ['name_form1',
                  'name_form2','name_form3','name_form4','name_form5','name_form6',
                  'name_form7','name_form8','name_form9','name_form10','name_form11','value2','value3']

    # widgets = {
    #     "value1": TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Видимость формы 1',
    #         'label':'Видимость формы 1'
    #     }),
    #     "value2": TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Видимость формы 1',
    #         'label': 'Видимость формы 1'
    #     }),
    # }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'


class ProfileForm(forms.ModelForm):
    """Форма профиля"""

    class Meta:
        model = ProfileUserModel
        fields = ['name_form1',
                  'name_form2', 'name_form3', 'name_form4', 'name_form5', 'name_form6',
                  'name_form7', 'name_form8', 'name_form9', 'name_form10', 'name_form11', 'value2', 'value3']
        # fields = ('__all__')

    # widgets = {
    #     "value1": TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Видимость формы 1',
    #         'label': 'Видимость формы 11'
    #     }),
    #     "value2": TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Видимость формы 1',
    #         'label': 'Видимость формы 1'
    #     }),
    # }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'

class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user



