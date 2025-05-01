from django.db import models

MAX_LENGTH = 255

class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Flower(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название')  # Название цветка или букета
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    photo = models.ImageField(upload_to='flowers/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_available = models.BooleanField(default=True, verbose_name='В наличии?')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return f'{self.name} - {self.price} руб.'

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы'

class Supplier(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название поставщика')
    contact_email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.TextField(verbose_name='Адрес')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

class Delivery(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название службы доставки')
    cost = models.FloatField(verbose_name='Стоимость доставки')
    estimated_time = models.CharField(max_length=MAX_LENGTH, verbose_name='Примерное время доставки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Служба доставки'
        verbose_name_plural = 'Службы доставки'

class Review(models.Model):
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, verbose_name='Цветок')
    customer_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя клиента')  # Заменяем User на строку
    rating = models.PositiveIntegerField(verbose_name='Оценка', choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отзыва')

    def __str__(self):
        return f"Отзыв на {self.flower.name} от {self.customer_name}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Promotion(models.Model):
    title = models.CharField(max_length=MAX_LENGTH, verbose_name='Название акции')
    description = models.TextField(verbose_name='Описание')
    discount = models.FloatField(verbose_name='Скидка (%)')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')
    banner = models.ImageField(upload_to='promotions/%Y/%m/%d', null=True, blank=True, verbose_name='Баннер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    working_hours = models.CharField(max_length=100, verbose_name='Часы работы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

class Employee(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя сотрудника')
    position = models.CharField(max_length=MAX_LENGTH, verbose_name='Должность')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name='Магазин')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'