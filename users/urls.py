"""为应用程序users定义URL模式"""

from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView

from . import views


urlpatterns = [
    #登陆页面
    #re_path('^login/$', login, {'template_name':'users/login.html'}, name='login'),
    re_path('^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    #注册页面
    re_path('^register/$',views.register,name='register'),
    #注销
    re_path('^logout/$',views.logout_view,name='logout'),
    #显示所有主题
    #re_path('^topics$',views.topics,name='topics'),
    #特定主题的详细页面
    #re_path('^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
]

app_name = 'users'