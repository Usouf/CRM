from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200, null = True)
    phone = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    profile_pic = models.ImageField(default = "user.svg", null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = [
		('Indoor', 'Indoor'),
		('Out Door', 'Out Door'),
	]
    name = models.CharField(max_length = 200, null = True)
    price = models.FloatField(null = True)
    category = models.CharField(max_length = 200, null = True, choices = CATEGORY)
    description = models.CharField(max_length = 200, null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    tag = models.ManyToManyField(Tag)
    class Meta:
        permissions = [
            ("change_product_price", "can change product price only")
        ]
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    ]
    customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL)
    product = models.ForeignKey(Product, null = True, on_delete = models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    status = models.CharField(max_length = 200, null = True, choices = STATUS)

    def __str__(self):
        return self.product.name

    def getProductName(self):
        return self.product.name

    def getDateTime(self):
        return self.date_created.strftime("@ %H:%M:%S on %m/%d/%Y")

class FileUpload(models.Model):
    title = models.CharField(max_length = 80, null = True)
    file = models.FileField(null = True, upload_to='documents/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title
