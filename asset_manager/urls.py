from django.conf.urls import url
from django.urls import path, include

from asset_manager.views import views, employee, employer

urlpatterns = [
    url('^$', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/signup/', account.SignUpView.as_view(), name='signup'),
    path('accounts/signup/employee/', employee.EmployeeSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/employer/', employer.EmployerSignUpView.as_view(), name='teacher_signup'),
]
