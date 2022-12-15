# class_based_view/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

home_context = {'title': 'Home',
                'h1': 'Home Page'}

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html', extra_context=home_context)),
    path('admin/', admin.site.urls),
    path('cbv/', include('cbv.urls'))
]
