from django.contrib import admin
from .models import *


admin.site.register(category)
admin.site.register(products)
admin.site.register(customer)
admin.site.register(owners)
admin.site.register(CartItem)