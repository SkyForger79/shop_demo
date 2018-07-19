# импортируем из джанго методы добавления в админку  
from django.contrib import admin 
# импортируем нашу модель
from .models import Product

# говорим админке зарегистрировать нашу модель
admin.site.register(Product)
