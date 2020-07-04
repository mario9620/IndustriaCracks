from django.db import models

# Create your models here.
class Direction(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.TextField()
    relative_location = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    birth_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField()
    is_superuser = models.BooleanField()
    user_image = models.CharField(max_length=255)
    cover_image = models.CharField(max_length=255)
    join_date = models.DateTimeField(auto_now_add=True)
    direction_id = models.ForeignKey(Direction, related_name='directions', on_delete=models.CASCADE)

    def __str__(self):
        return f'name: {self.first_name}'

class Followers(models.Model):
    id = models.AutoField(primary_key=True)
    follower_id = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    followed_id = models.ForeignKey(User, related_name='followed', on_delete=models.CASCADE)
    follow_date = models.DateTimeField(auto_now_add=True)
    puntuation = models.IntegerField()

class Complaints(models.Model):
     id = models.AutoField(primary_key=True)
     date = models.DateTimeField(auto_now_add=True)
     denounced_user_id = models.ForeignKey(User, related_name='denounced_user', on_delete=models.CASCADE)
     accuser_user_id = models.ForeignKey(User, related_name='accuser_user', on_delete=models.CASCADE)


class Currency(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Currency: {self.name}"

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Category: {self.name}"

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    img_route = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    currency_id = models.ForeignKey(Currency, related_name='currency_product', on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, related_name='category_product', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, related_name='user_owner', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Product: {self.name}"

class Image_Product(models.Model):
    images_id = models.ForeignKey(Image, related_name='image_route', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, related_name='products_images', on_delete=models.CASCADE)

class Status(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Status of Order: {self.description}"

class shipping_method(models.Model):
    id = models.AutoField(primary_key=True)
    method_description = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Shipping method: {self.method_description}"

class payment_method(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    status_id = models.ForeignKey(Status, related_name='status_order', on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    isv = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    direction_id = models.ForeignKey(Direction, related_name='direction_order', on_delete= models.CASCADE)
    shipping_method_id = models.ForeignKey(shipping_method, related_name='shipping_method_order', on_delete= models.CASCADE)
    payment_method_id = models.ForeignKey(payment_method, related_name='payment_method_order', on_delete=models.CASCADE)


class product_order(models.Model):
    product_id = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, related_name='orders', on_delete=models.CASCADE)

class payment_data(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    credit_card_number = models.BigIntegerField()
    expiration_date = models.DateTimeField(auto_now=True)
    cvv = models.IntegerField()
    payment_method_id = models.ForeignKey(payment_method, related_name='payment_method', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, related_name='user_payment_data', on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

class Action(models.Model):
    id = models.AutoField(primary_key=True)
    crud_type = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

class Log(models.Model):
    id = models.AutoField(primary_key=True)
    action = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    user_id = models.ForeignKey(User, related_name='user_log', on_delete=models.CASCADE)
    action_id = models.ForeignKey(Action, related_name='action_log', on_delete=models.CASCADE)

