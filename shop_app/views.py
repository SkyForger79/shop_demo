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

from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy
from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# импортируем нашу модель
from .models import Product, Category, Order
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

#вью для создания форм
class ProductCreate(generic.CreateView): 
	model = Product 
	# название нашего шаблона с формой
	template_name = 'product_new.html' 
	# какие поля будут в форме 
	fields = '__all__'

#вью для создания заказа
class OrderFormView(LoginRequiredMixin, generic.CreateView): 
    model = Order
    template_name = 'order_form.html' 
    success_url = '/' 
    fields = ['customer_name','customer_phone']
    
    #метод валидации формы
    def form_valid(self, form):
        # получаем ID из ссылки и передаем в ORM для фильтрации
        product = Product.objects.get(id=self.kwargs['pk']) 
        user = self.request.user 
        form.instance.user = user
        # передаем в поле товара нашей формы отфильтрованный товар
        form.instance.product = product 
        # super — перезагружает форму, нужен для работы
        return super().form_valid(form)
      
 #вью для формы регистрации
class SignUpView(generic.CreateView): 
    form_class = UserCreationForm 
    success_url = reverse_lazy('login') 
    template_name = 'signup.html'

# наш секретный Вью
class SecretAdminView(UserPassesTestMixin, generic.TemplateView):
    # секретное содержимое
    template_name = 'memes.html'
	# проверяем условие, если пользователь — админ, то вернет True и пустит пользователя
    def test_func(self):
        return self.request.user.is_superuser