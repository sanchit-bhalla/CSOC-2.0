from django.urls import re_path
from register_app.views import register,user_login,about,discussions

app_name='register_app'

urlpatterns = [
    re_path(r'^register/', register, name='register'),
    re_path(r'^user_login/', user_login,name='user_login'),
    re_path(r'^about/', about,name='about'),
    re_path(r'^discussions/', discussions,name='discussions'),
]
