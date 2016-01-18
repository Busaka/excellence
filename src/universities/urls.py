


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
from universities import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'local_universities$', views.local_universities, name='local_universities'),
    url(r'(?P<uni_id>\d+)/local_uni_details/$', views.local_university_details, name='local_uni_details'),
    url(r'international_universities$', views.international_universities, name='international_universities'),
    url(r'(?P<uni_id>\d+)/international_uni_details/$', views.international_uni_details, name='international_uni_details'),
]
