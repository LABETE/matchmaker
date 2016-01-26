from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from newsletter.views import homeTemplateView


urlpatterns = [
    # Examples:
    url(r'^$', homeTemplateView.as_view(), name='home'),
    url(r'^jobs/', include('jobs.urls', namespace="jobs")),
    url(r'^like/', include('likes.urls', namespace="like")),
    url(r'^profiles/', include('profiles.urls', namespace="profiles")),
    url(r'^questions/', include('questions.urls', namespace="questions")),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'matchmaker.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)