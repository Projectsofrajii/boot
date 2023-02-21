from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView

from .import views

urlpatterns = [
    path('createlist/',views.sampleboot),
    path("", TemplateView.as_view(template_name="test/first.html"), name="home"),  # direct access to temp

]