
from django.contrib import admin
from django.urls import path, re_path
from libs import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/tickets/$', views.tickets_list),
]
