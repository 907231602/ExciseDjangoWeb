"""ExciseDjangoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from myApp import views as myapp_view
from learn import views as learn_view



urlpatterns = [
    path('', myapp_view.index, name='home'),
    path('admin/', admin.site.urls),
    #path('myapp/',include('myApp.urls')),
    #path('myapp/',include(urls))
    path('add/', myapp_view.add, name='add'),  # new
    path('new_add2/<int:a>/<int:b>/', myapp_view.add2, name='add2'),
    path('learn',learn_view.home,name='learnHome'),
    path('base',learn_view.base,name='learnBase'),
    path('tmup',learn_view.showString,name='showstring'),
    path('forlist',learn_view.forList,name='forlist'),
    path('shoedict',learn_view.showDict,name='showdict'),
    path('iffor',learn_view.ifFor,name='iffor'),

]
