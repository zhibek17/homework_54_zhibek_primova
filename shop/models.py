from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, unique=True, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Наименование')
    description = models.TextField(max_length=400, null=True, blank=True, verbose_name='Описание')
    category = models.ForeignKey('shop.Category', on_delete=models.RESTRICT, verbose_name='Категория')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.title



