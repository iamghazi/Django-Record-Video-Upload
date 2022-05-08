from django import forms
from django.views.generic.edit import FormView
import tempfile
from django.http import HttpResponse, HttpResponseBadRequest


class YouTubeForm(forms.Form):
    video = forms.FileField()


class HomePageView(FormView):
    template_name = 'core/home.html'
    form_class = YouTubeForm

    def handle_uploaded_file(self, f):
        with open('record.webm', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    def form_valid(self, form):
        request = self.request
        if request.method == 'POST':
            form = YouTubeForm(request.POST, request.FILES)
            if form.is_valid():
                # print(request.FILES['video'].read())
                self.handle_uploaded_file(request.FILES['video'])
                return HttpResponse('It worked!')
            # return HttpResponseRedirect('/success/url/')


