# импортируем из джанго методы добавления в админку  
from django.contrib import admin 
# импортируем наши модели
from .models import Product, Category, Order


# говорим админке зарегистрировать нашу модель
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
