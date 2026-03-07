from django.db import models

# Create your models here.

# Class named Product with fields: title, description, price, inventory, last_update
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    # stock = models.IntegerField()

# Class named Customer with fields: first_name, last_name, email, phone, birth_date
class Customer(models.Model):

    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        ('B', 'Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

class Order(models.Models):
    PAYMETN_STATUS_PENDING = 'P'
    PAYMETN_STATUS_COMPLETE = 'C'
    PAYMETN_STATUS_FAILED = 'F'
    PAYMETN_STATUS_CHOICES = [
        (PAYMETN_STATUS_PENDING, 'Pending'),
        (PAYMETN_STATUS_COMPLETE, 'Complete'),
        (PAYMETN_STATUS_FAILED, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMETN_STATUS_CHOICES, default=PAYMETN_STATUS_PENDING)