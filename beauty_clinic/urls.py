"""
URL configuration for beauty_clinic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_page'),
    path('', include('home.urls')),
    path('services/', include('services.urls')),
    path('team/', include('team.urls')),
    path('account/', include('account.urls')),
    path('user-panel/', include('user_panel.urls')),
    path('blogs/', include('blog.urls')),
    path('about-us/', include('about_us.urls')),
    path('contact-us', include('contact_us.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
