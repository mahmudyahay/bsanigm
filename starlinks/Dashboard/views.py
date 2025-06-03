from django.shortcuts import render, redirect
from .models import *
from datetime import timedelta
from django.utils import timezone

# Create your views here.
def is_active(id, email):
    try:
        check = owners.objects.get(id=id, email=email)
        return True
    except owners.DoesNotExist:
        return False
    

def product(request):
    try:
        is_active(request.session['admin_id'], request.session['email'])
        store = products.objects.all()
        categories = category.objects.all()  # to send categories to the template
        

        if request.method == 'POST':
            action = request.POST.get('action')

            if action == 'add':
                Name = request.POST.get('Name')
                category_id = request.POST.get('category')  # ID of selected category
                price = request.POST.get('price')
                stock = request.POST.get('stock')
                discount = request.POST.get('discount')
                image = request.FILES.get('image')  # corrected from FILEs to FILES
                status = request.POST.get('status')
                discription = request.POST.get('discription')

                # Convert category ID to actual Category object
                selected_category = category.objects.get(id=category_id)

                products.objects.create(
                    Name=Name,
                    category=selected_category,
                    stock=stock,
                    price=price,
                    discount=discount,
                    image=image,
                    status=status,
                    description = discription,
                    createdat = timezone.now()
                )

                return redirect('product')  # better to redirect to avoid form resubmission
            if action == 'edit':
                product_id = request.POST.get('product_id')
                p = products.objects.get(id=product_id)

                p.Name = request.POST.get('Name')
                p.category = category.objects.get(id=request.POST.get('category'))
                p.price = request.POST.get('price')
                p.discount = request.POST.get('discount')
                p.stock = request.POST.get('stock')
                p.status = request.POST.get('status')
                p.description = request.POST.get('discription')

                # Only update image if a new one was uploaded
                if request.FILES.get('image'):
                    p.image = request.FILES.get('image')

                p.save()
                return redirect('product')
            elif action == 'delete':
                product_id = request.POST.get('product_id')
                p = products.objects.get(id=product_id)
                p.delete()
                return redirect('product')
    except KeyError:
        return render(request, 'login.html')

    return render(request, 'product.html', {'product': store, 'categories': categories, })

def categories(request):
    try:
        is_active(request.session['admin_id'], request.session['email'])
        cat = category.objects.all()
        if request.method == 'POST':
            action = request.POST['action']
            if action == 'add':
                name = request.POST['name']
                discription = request.POST.get('discription')
                image = request.FILES.get('image')
                category.objects.create(name=name, discription=discription, image=image)
                return redirect('categories')
            if action == 'edit':
                cid = request.POST['cid']
                ed = category.objects.get(id=cid)
                name = request.POST['name']
                discription = request.POST['discription']
                image = request.FILES.get('image', ed.image)
                ed.name = name
                ed.image = image
                ed.discription = discription
                ed.save()
                return redirect('categories')
            if action == 'del':
                cid = request.POST['cid']
                dl = category.objects.get(id=cid)
                dl.delete()
                return redirect('categories')
            
        return render(request, 'categories.html', {'cat':cat})
    except KeyError:
        return render(request, 'login.html')


def Dashboard(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            owner = owners.objects.get(username=username, password=password)
            request.session['admin_id'] = owner.id
            request.session['email'] = owner.email
            return redirect('product')
        except owners.DoesNotExist:
            return render(request, 'login.html', {'error':'wrong details'})
    try:
        id = request.session['admin_id']
        try:
            admin = owners.objects.get(id=id)
            return render(request, 'dashboard.html')
        except owners.DoesNotExist:
            return render(request, 'login.html')
    except KeyError:
        return render(request, 'login.html')


