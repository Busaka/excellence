"""phan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from excellence_jobs import views

urlpatterns = [
    url(r'^$', views.kazi, name='home'),
    url(r'^post_job/', views.post_kazi, name='post_job'),
    url(r'(?P<job_id>\d+)/job_details/$', views.kazi_details, name='job_details'),
    url(r'(?P<job_title>[\w\s]+[\w\s]+[\w])/available_jobs/$', views.available_jobs, name='available_jobs'),
]
