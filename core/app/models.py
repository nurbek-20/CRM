from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Manager(models.Model):
    full_name = models.CharField(
        max_length=100
    )
    phone_number = models.CharField(
        max_length=20
    )
    email = models.EmailField()
    created_date = models.DateField(
        auto_now_add=True
    )
    number_of_deals = models.IntegerField()
    temporary_password = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.full_name


class Client(models.Model):
    status_choices = (
        ('active', 'Активно'),
        ('reserved', 'Бронь'),
        ('sold', 'Продано'),
        ('instalment', 'Рассрочка'),
        ('barter', 'Бартер'),
    )
    full_name = models.CharField(
        max_length=100
    )
    contact_number = models.CharField(
        max_length=20
    )
    contract_number = models.CharField(
        max_length=50
    )
    status = models.CharField(
        max_length=20,
        choices=status_choices
    )

    def __str__(self):
        return f"{self.full_name} - {self.status}"


class ObjectName(models.Model):
    title = models.CharField(
        max_length=125
    )

    def __str__(self):
        return self.title


class Apartment(models.Model):
    number = models.IntegerField()
    object_name = models.ForeignKey(
        ObjectName,
        on_delete=models.CASCADE)
    floor = models.IntegerField()
    square_meters = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Метр в квадрате'
    )
    date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=Client.status_choices,
        default='active')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='В сомах',
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Apartment №{self.number}, Status: {self.status}"






