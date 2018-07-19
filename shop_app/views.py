from django.shortcuts import render
# импортируем из стандартной сборки Django
from django.http import HttpResponse 

# Стандартный вью — это обычная питон-функция, которая получает аргумент request
def index(request):
    request_method = request.method
    
    ip_address = request.META['REMOTE_ADDR']
    browser_info = request.META['HTTP_USER_AGENT']
    
    # импортируем модель для CBV            
from django.views import generic 

# импортируем нашу модель
from .models import Product

class ProductListView(generic.ListView): 

  template_name = 'products_list.html' # подключаем наш Темплейт
  context_object_name = 'products' # под каким именем передадутся данные в Темплейт
  model = Product # название Модели