"""lighting_talks_scheduler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .views import homepage, NameView, EmailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('name/', NameView.as_view(), name='name'),
    path('email/', EmailView.as_view(), name='email'),
    # todo - Rachel's next trello board ticket
    # path('email/', EmailView.as_view(), name='email')
]
