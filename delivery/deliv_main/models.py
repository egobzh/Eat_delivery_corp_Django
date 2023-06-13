from django.db import models
from datetime import date

class Worker(models.Model):
    name = models.CharField('Имя работника',max_length=100)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name='Работник'
        verbose_name_plural="Работники"

class Food(models.Model):
    name = models.CharField('Название блюда',max_length=130)
    structure = models.TextField('Состав блюда',max_length=2000)
    price = models.FloatField()
    def __str__(self):
        return f'{self.name},{self.price}'

    class Meta:
        verbose_name='Блюдо'
        verbose_name_plural="Блюда"

class Order(models.Model):
    date = models.DateField(default=date.today)
    order_worker = models.ForeignKey(Worker,verbose_name='Сотрудник',on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.date},{self.order_worker}'

    class Meta:
        verbose_name='Заказ'
        verbose_name_plural="Заказы"

class Food_order(models.Model):
    orderr = models.ForeignKey(Order, verbose_name='Заказ', on_delete=models.CASCADE)
    order_food = models.ForeignKey(Food, verbose_name='Блюда', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.orderr}'

    class Meta:
        verbose_name='Состав заказа'
        verbose_name_plural="Состав заказов"