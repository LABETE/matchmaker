from django.conf.urls import url

from .views import LikeRedirectView


urlpatterns = [
    # Examples:
    url(r'^(?P<pk>\d+)/$', LikeRedirectView.as_view(), name="detail"),
]