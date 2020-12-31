"""bookstore_project URL Configuration

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
from django.conf import settings # new
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #Django Admin
    path('admin/', admin.site.urls),

    

    # User Management
    # path('accounts/', include('django.contrib.auth.urls')), # new  use Django’s built-in auth app we must explicitly add it to our bookstore_- project/urls.py file

    # path('accounts/', include('users.urls')), # new  it’s common to use the same accounts/ one used by the default auth app

    path('accounts/', include('allauth.urls')), # new  o swap out the built-in auth app URLs for django-allauth’s own allauth app


    # Local apps
    path('', include('pages.urls')),
    path('books2/', include('books2.urls')), # new
    path('orders/', include('orders.urls')), # new
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # new


# to see media items locally we need to update bookstore_project/urls.py to show the
# files locally
# to see media items locally we need to update bookstore_project/urls.py to show the
# files locally