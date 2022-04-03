from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings
from uuid import uuid4
# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']


class RestaurantCollections(models.Model):
    title = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.CharField(max_length=255)
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(
        Collection, on_delete=models.PROTECT, related_name='products')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class Customer(models.Model):
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )

    class Meta:
        unique_together = [['cart', 'product']]


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
