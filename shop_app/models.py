# Импортируется родительский класс моделей            
from django.db import models 

# Создаем базовую модель нашего продукта
class Product(models.Model): 
  title = models.CharField(max_length=200) # и указываем максимальную длину
  description = models.TextField(max_length=5000)

  def __str__(self):
    return self.title