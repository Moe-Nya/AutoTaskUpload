#子路由
from django.urls import path, re_path
from hw import views
from django.conf.urls import url
from django.views import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'), 
    re_path(r'^student/$',views.student),
    re_path(r'^upload/$',views.upload),
    url(r'^static/(?P<path>.*)$', static.serve,
      {'document_root': settings.STATIC_ROOT}, name='static'),
]