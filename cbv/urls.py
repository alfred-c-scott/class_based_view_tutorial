from django.urls import path
from django.views.generic import TemplateView

from .views import Ex2View

ex1_context = {'title': 'ex1',
               'h1': 'Greetings this is the ex1 template'}

app_name = 'cbv'

urlpatterns = [
    path('ex1/', TemplateView.as_view(template_name='cbv/ex1.html', extra_context=ex1_context)),
    path('ex2/', Ex2View.as_view(), name='ex2')
]
