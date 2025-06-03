from django.db import models

class category(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=300)
    image = models.ImageField(upload_to='static/images')

class products(models.Model):
    Name = models.CharField(max_length=100)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    price = models.CharField(max_length=100)
    stock = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    status = models.CharField(max_length=100)
    createdat = models.DateTimeField(default='2024-12-12')
    description = models.CharField(max_length=10000)

class customer(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=6)
    state = models.CharField(max_length=100)
    LGA = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    shipingadress = models.CharField(max_length=200)
    option = [('True','True'), ('False','False')]
    is_active = models.CharField(max_length=100, choices=option)

class CartItem(models.Model):
    cart = models.ForeignKey(customer, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class order(models.Model):
    s_choice = [('ORDERED', 'ORDERED'), ('SHIPPED', 'SHIPPED'), ('DELIVERD', 'DELIVERD')]
    user = models.ForeignKey(customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=0)
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=s_choice)

    class meta:
        odering = ('-created_at')
    
    def __str__(self):
        return f'F{self.user}'

class order_iterms(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'F{self.order} {self.product}'

class owners(models.Model):
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    phone = models.CharField(max_length=11)
    