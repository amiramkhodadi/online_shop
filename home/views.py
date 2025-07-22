from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePage(TemplateView):
    template_name = "home/index.html"
    # def get_context_data(self, **kwargs):
    #   context = super().get_context_data(**kwargs)
    #   self.request.session.get('my_name' , 'amir')
    #   print(self.request.session.get('my_name' , 'amir'))
    #   return context




