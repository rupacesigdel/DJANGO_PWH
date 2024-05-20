from django.contrib import admin
from django.urls import path, include
from home import views

#  django admin header customization 

admin.site.site_header = " Login to Developer Rupesh"
admin.site.site_title = "Welcome to rupesh Dashboard"
admin.site.index_title = "Welcome to this Portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('project', views.project, name='project'),
    path('contact', views.contact, name='contact'),
]
