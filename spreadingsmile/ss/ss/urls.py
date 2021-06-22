"""ss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from home import views as home_view
from volunteers import views as volunteers_view
from events import views as events_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view.home,name='home'),
    path('donationform/',home_view.donation,name='donationform'),

    path('volunteerform/',volunteers_view.volunteerform,name='volunteerform'),
    path('volunteers/',volunteers_view.registeredvolunteers,name='volunteers'),
    path('acceptvolunteer/<int:volunteer_pk>',volunteers_view.acceptvolunteer,name='acceptvolunteer'),
    path('rejectvolunteer/<int:volunteer_pk>',volunteers_view.rejectvolunteer,name='rejectvolunteer'),

    path('upcomingevents/',events_view.upcomingevents,name='upcomingevents'),
    path('upcomingevents/<int:event_pk>',events_view.detail,name='detail'),
    
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)