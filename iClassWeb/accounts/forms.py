from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Teacher, Student
from django.contrib.auth import get_user_model
from django.db import transaction



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')


class StudentSignupForm(CustomUserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(CustomUserCreationForm.Meta):
        User = get_user_model()
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        student = Student.objects.create(user=user)
        return user


class TeacherSignupForm(CustomUserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(CustomUserCreationForm.Meta):
        User = get_user_model()
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        teacher = Teacher.objects.create(user=user)
        return user


