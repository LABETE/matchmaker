from django.conf.urls import url

from .views import (ProfileDetailView,
                    UserJobCreateView,
                    UserJobUpdateView,
                    UserProfileDetailView,
                    UpdateProfile)


urlpatterns = [
    url(r'^create/$', UserJobCreateView.as_view(), name='create'),
    url(r'^editjobs/$', UserJobUpdateView.as_view(), name='update'),
    url(r'^profile/(?P<slug>[\w-]+)/$', UserProfileDetailView.as_view(), name='my_profile'),
    url(r'^profile/(?P<slug>[\w-]+)/edit/$', UpdateProfile.as_view(), name='edit_profile'),
    url(r'^(?P<slug>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
]
