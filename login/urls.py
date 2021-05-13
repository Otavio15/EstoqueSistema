from django.urls import path

from .views import login_page, login_submit

urlpatterns = [
    path('', login_page, name='login'),
    path('submit', login_submit, name='login-submit'),
]
