"""HttpTestProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, path
from HttpTest import views as HttpTest_views

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^$', HttpTest_views.index, name='index'),
    path('POST.html', HttpTest_views.post_test, name='post_test'),

    re_path(r'^URL.html$', HttpTest_views.url_test, name='url_test'),
    path('test.html', HttpTest_views.test, name='test'),
]
