from django.shortcuts import render, redirect
from django.urls import reverse
from Dashboard.models import *
from datetime import timedelta
from django.utils import timezone
import random
from django.contrib import messages

def Home(request):
    time_threshold = timezone.now() - timedelta(hours=48)

    recent_products = products.objects.filter(createdat__gte=time_threshold)
    cat = category.objects.all()
    

    # Get all products
    all_products = list(products.objects.all())
    sample_size = len(all_products) // 2
    random_products = random.sample(all_products, sample_size) if sample_size > 0 else []

    # Get category objects
    surveillance_cat = category.objects.filter(name__icontains="Surveillance").first()
    internet_cat = category.objects.filter(name="Internet & Satellite Equipment").first()

    # Best products from both categories
    best_surveillance = []
    best_internet = []

    if surveillance_cat:
        surveillance_products = list(products.objects.filter(category=surveillance_cat))
        best_surveillance = random.sample(surveillance_products, min(5, len(surveillance_products)))

    if internet_cat:
        internet_products = list(products.objects.filter(category=internet_cat))
        best_internet = random.sample(internet_products, min(5, len(internet_products)))
    
    best = []
    for x in best_internet:
        best.append(x)
    for x in best_surveillance:
        best.append(x)
    
    
    try:
        users = customer.objects.get(id=request.session['id'])
        user = 'True'
        admin = users
    except KeyError:
        user = 'False'
        admin = ''
    
    try:
        carts = CartItem.objects.filter(cart=customer.objects.get(id=request.session['id']))
    except KeyError:
        carts = []
               
    cart = []
    sum = 0
    num = 0

    for x in carts:
        x.total_price = int(x.product.price) * int(x.quantity ) # Create a temporary field
        cart.append(x)
        sum += x.total_price
        num +=1

    content = {
        'cat': cat,
        'product': random_products,
        'recent_products': recent_products,
        'best':best,
        'user':user,
        'cart':cart,
        'sum':sum,
        'num':num,
        'admin':admin,

    }
    return render(request, 'index.html', content)

def addcart(request):
    if request.method == 'POST':
        try:
            try:
                id = request.session['id']
            except KeyError:
                messages.error(request, "signup please")
                return redirect('Home')
            cus = customer.objects.get(id=id)
            cart = cus
            pid = request.POST['pid']
            quantity = request.POST['quantity']
            try:
                check = CartItem.objects.get(cart=cart, product= products.objects.get(id=pid))
                check.quantity = quantity
                check.save()
            except CartItem.DoesNotExist:
                CartItem.objects.create(cart=cart, product= products.objects.get(id=pid), quantity=quantity)
            return redirect('Home')
        except customer.DoesNotExist:
            pass

    return redirect('Home')

def signup(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            check = customer.objects.get(email=email)
            messages.error(request, "user alredy exis")
            url = reverse('Home') + '#signup'
            return redirect(url)
        except customer.DoesNotExist:
            customer.objects.create(email=email, password=password)
        
        co = customer.objects.get(email=email)
        request.session['id'] =co.id
        return redirect('Home')
    
def search(request):
    if request.method == 'POST':
        cart = request.POST['cart']
        cat = category.objects.get(name=cart)
        product = products.objects.filter(category=cat)

        try:
            users = customer.objects.get(id=request.session['id'])
            user = 'True'
        except KeyError:
            user = 'False'
        
        try:
            carts = CartItem.objects.filter(cart=customer.objects.get(id=request.session['id']))
        except KeyError:
            carts = []
                
        cart = []
        sum = 0
        num = 0

        for x in carts:
            x.total_price = int(x.product.price) * int(x.quantity ) # Create a temporary field
            cart.append(x)
            sum += x.total_price
            num +=1

        content = {
            'cat': category.objects.all(),
            'product': product,
            'user':user,
            'cart':cart,
            'sum':sum,
            'num':num

        }
    return render(request, 'search.html', content)

def searcht(request):
    if request.method == 'POST':
        cat = request.POST['name']
        produc = products.objects.all()
        product = []
        for x in produc:
            if cat in x.Name:
                product.append(x)

        try:
            users = customer.objects.get(id=request.session['id'])
            user = 'True'
        except KeyError:
            user = 'False'
        
        try:
            carts = CartItem.objects.filter(cart=customer.objects.get(id=request.session['id']))
        except KeyError:
            carts = []
                
        cart = []
        sum = 0
        num = 0

        for x in carts:
            x.total_price = int(x.product.price) * int(x.quantity ) # Create a temporary field
            cart.append(x)
            sum += x.total_price
            num +=1

        content = {
            'cat': category.objects.all(),
            'product': product,
            'user':user,
            'cart':cart,
            'sum':sum,
            'num':num

        }
        return render(request, 'search.html', content)

def removecart(request, id):
    cart = CartItem.objects.get(id=id)
    cart.delete()
    return redirect('Home')

def editadmin(request):
    admin = customer.objects.get(id=request.session['id'])
    if request.method == 'POST':
        admin.username = request.POST['username']
        admin.email = request.POST['email']
        admin.state = request.POST.get('state', '')
        admin.LGA = request.POST.get('lga', '')
        admin.shipingadress = request.POST.get('shipping_address', '')
        admin.phone = request.POST.get('phone', '')
        admin.save()
        return redirect('Home')

def login(request):
    if request.method=='POST':
        email = request.POST['email']
        passwod= request.POST['password']

        try:
            c = customer.objects.get(email=email, passwod=passwod)
            request.session['id']=c.id
            return redirect('Home')
        except customer.DoesNotExist:
            return redirect('Home') + '#signup'

def Order(request):
    if request.method == 'POST':
        pass