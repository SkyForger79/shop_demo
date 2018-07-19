"""shop_project URL Configuration

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
# стандартный вью для админки
from django.contrib import admin
# модуль Джанго для определения URL'ов
from django.urls import path 
# импортируем наш файл views из shop_app
from shop_app import views 

# говорим Джанго о том, что хотим отображать наш вью на главной странице
# а строчкой ниже, кстати ссылка на нашу админку, про нее позже
urlpatterns = [ 
  path('', views.ProductListView.as_view(),name='index'), 
  path('admin/', admin.site.urls),
]
