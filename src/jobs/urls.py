from django.conf.urls import url

from .views import JobDetailView, LocationDetailView, EmployerDetailView


urlpatterns = [
    # Examples:
    url(r'^position/(?P<slug>[\w-]+)/$', JobDetailView.as_view(), name='job_detail'),
    url(r'^location/(?P<slug>[\w-]+)/$', LocationDetailView.as_view(), name='location_detail'),
    url(r'^employer/(?P<slug>[\w-]+)/$', EmployerDetailView.as_view(), name='employer_detail'),
]