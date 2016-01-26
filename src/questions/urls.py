from django.conf.urls import url

from .views import QuestionDetailView


urlpatterns = [
    # Examples:
    url(r'^question/(?P<pk>\d+)/$', QuestionDetailView.as_view(), name='detail'),
]