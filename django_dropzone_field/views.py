from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import TemporaryUploadForm


class TemporaryUploadView(CreateView):
    form_class = TemporaryUploadForm

    def form_valid(self, form):
        instance = form.save()
        return HttpResponse(instance.hash)


