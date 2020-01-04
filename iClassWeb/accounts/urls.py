from django.urls import path, re_path, include
from . import views
from django.contrib.auth import views as auth_views
from accounts.views import SignupView, TeacherSignupView, StudentSignupView, View_Profile, Edit_Profile, Delete_Account


urlpatterns = [
	path('', views.index, name='index'),
	path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('signup/', SignupView.as_view(), name='signup'),
	path('signup/teacher/', TeacherSignupView.as_view(), name='teacher_signup'),
	path('signup/student/', StudentSignupView.as_view(), name='student_signup'),
	path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/change_pass.html'), name='password_change'),
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/change_pass_done.html'), name='password_change_done'),
	path('profile/', View_Profile.as_view(), name='view_profile'),
    path('', include('django.contrib.auth.urls')),
	re_path(r'^profile/edit/(?P<pk>\d+)/$', Edit_Profile.as_view(), name='edit_profile'),
	re_path(r'^delete/(?P<pk>\d+)/$', Delete_Account.as_view(), name='delete_account')
]