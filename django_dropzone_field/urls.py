from django.conf.urls import patterns, url
from .views import TemporaryUploadView

urlpatterns = patterns('',
    url(r'^temporary-upload/$', TemporaryUploadView.as_view(), name='upload'),
)