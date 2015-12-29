from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
import high_schools.urls
import contact.urls
import jobs.urls
import magazine.urls
import colleges.urls
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^high_schools', include(high_schools.urls, namespace='high_schools')),
    url(r'^contact', include(contact.urls, namespace='contact')),
    url(r'^jobs', include(jobs.urls, namespace='jobs')),
    url(r'^magazine', include(magazine.urls, namespace='magazine')),
    url(r'^colleges', include(colleges.urls, namespace='colleges')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
