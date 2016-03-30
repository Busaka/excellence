from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
import high_schools.urls
import excellence_profile.urls
import contact.urls
import excellence_jobs.urls
import magazine.urls
import news.urls
import colleges.urls
import universities.urls
import membership.urls
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^excellence_profile/', include(excellence_profile.urls, namespace='excellence_profile')),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^high_schools/', include(high_schools.urls, namespace='high_schools')),
    url(r'^contact/', include(contact.urls, namespace='contact')),
    url(r'^excellence_jobs/', include(excellence_jobs.urls, namespace='excellence_jobs')),
    url(r'^magazine/', include(magazine.urls, namespace='magazine')),
    url(r'^news/', include(news.urls, namespace='news')),
    url(r'^colleges/', include(colleges.urls, namespace='colleges')),
    url(r'^universities/', include(universities.urls, namespace='universities')),
    url(r'^membership/', include(membership.urls, namespace='membership')),
    # url(r'^search/', include('haystack.urls')),
]

# User-uploaded files like profile pics need to be served in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
