from django.shortcuts import render
# импортируем из стандартной сборки Django
from django.http import HttpResponse 

# Стандартный вью — это обычная питон-функция, которая получает аргумент request
#def index(request):
#    request_method = request.method
#    
#    ip_address = request.META['REMOTE_ADDR']
#    browser_info = request.META['HTTP_USER_AGENT']
#    
    # импортируем модель для CBV            

from django.views import generic 

# импортируем нашу модель
from .models import Product, Category
#вью для списка категорий и продуктов для главной страницы
class CategoryListView(generic.ListView): 

  template_name = 'category_list.html' # подключаем наш Темплейт
  context_object_name = 'categories' # под каким именем передадутся данные в Темплейт
  model = Category # название Модели
  # метод для добавления дополнительной информации в контекст
  def get_context_data(self, **kwargs): 
      context = super().get_context_data(**kwargs)
      # передаем в словарь контекста список всех категорий 
      context['products'] = Product.objects.all()
      return context

#вью для деталей категории
class CategoryDetail(generic.DetailView): 
    template_name = 'category_detail.html' 
    model = Category
    def get_context_data(self, **kwargs): 
      context = super().get_context_data(**kwargs)
      # передаем в словарь контекста список всех категорий 
      context['products'] = Product.objects.all()
      return context


#вью для деталей продукта
class ProductDetail(generic.DetailView): 
    template_name = 'product_detail.html' 
    model = Product

