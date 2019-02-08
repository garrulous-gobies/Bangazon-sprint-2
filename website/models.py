from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator



#  ProductType model creation
class ProductType(models.Model):
    productCategory = models.CharField(max_length=50)
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self

# Create Product model.
class Product(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
    )
    title = models.CharField(max_length=80)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(validators=[MinValueValidator(.01)], max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    image = models.TextField(blank=True, null=True)
    productType = models.ForeignKey(
        ProductType,
        default = 0,
        on_delete=models.DO_NOTHING,
    )
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self

# Create Customer model.
class Customer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.DO_NOTHING,
        primary_key=True,
    )
    address = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self

# Create PaymentType model.
class PaymentType(models.Model):
    paymentCategory = models.CharField(max_length=50)
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self

# Create PaymentMethod model.
class PaymentMethod(models.Model):
    paymentName = models.ForeignKey(
        PaymentType,
        on_delete=models.DO_NOTHING,
    )
    customerPayment = models.ForeignKey(
        Customer,
        on_delete=models.DO_NOTHING,
    )
    accountNumber = models.PositiveIntegerField()
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self

# Create Order model.
class Order(models.Model):
    customerOrder = models.ForeignKey(
        Customer,
        on_delete=models.DO_NOTHING,
    )
    paymentOrder = models.ForeignKey(
        PaymentMethod,
        on_delete=models.DO_NOTHING,
    )
    Product = models.ManyToManyField(Product, through="ProductOrder")
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self

# Create ProductOrder model.
class ProductOrder(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.DO_NOTHING,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.DO_NOTHING,
    )
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self