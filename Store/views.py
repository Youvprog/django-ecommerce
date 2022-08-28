from re import T
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Product, Cart, Orderitems, Category,  VilleShipping, Filter, Color
from django.contrib import messages
from django.db.models import Max, Min
from .forms import Shipping
from django.core.mail import send_mail, EmailMessage
from django.template.loader import get_template


def product_filter_by_search(request):
    if request.method == 'POST':
        search_prod = request.POST['search_prod']
        products = Product.objects.filter(name = search_prod)
        return render(request, 'Store/includes/products_list.html',{
            "products":products
        })
    

def sort_prod(request, slug):
    categories = Category.objects.all()
    filters = Filter.objects.all()
    if slug == 'newest':
            prods = Product.objects.all().order_by("-id")
            return render(request,"Store/products.html", {
                "products" : prods,
                "categories" : categories,
                "filters": filters
            })
    elif slug == 'oldest':
            prods = Product.objects.all().order_by("id")
            return render(request,"Store/products.html", {
                "products" : prods,
                "categories" : categories,
                "filters": filters
            })
    elif slug == 'price-ascending':
            prods = Product.objects.all().order_by("price")
            return render(request,"Store/products.html", {
                "products" : prods,
                "categories" : categories,
                "filters": filters
                
            })
    elif slug == 'price-descending':
            prods = Product.objects.all().order_by("-price")
            return render(request,"Store/products.html", {
                "products" : prods,
                "categories" : categories,
                "filters": filters
            })
    elif slug == 'title-ascending':
            prods = Product.objects.all().order_by("name")
            return render(request,"Store/products.html", {
                "products" : prods,
                "categories" : categories,
                "filters": filters
            })
    elif slug == 'title-descending':
            prods = Product.objects.all().order_by("-name")
            return render(request,"Store/products.html", {
                "products" : prods,
                "categories" : categories,
                "filters": filters
            })

    else:
        prods = Product.objects.all()
        return render(request,'Store/products.html',{
            "products" : prods,
            "categories" : categories,
            "filters": filters
        })


def sort_with_colors(request,pk):
    products = Product.objects.filter(colors__id=pk)
    return render(request,'Store/includes/products_list.html', {
        "products": products
    })


def categorize_product(request,pk):
    products = Product.objects.filter(categories__id=pk)
    return render(request,'Store/includes/products_list.html',{
        "products" : products,
    })


def products_list(request):
    prices = Product.objects.all().aggregate(Max('price'), Min('price'))
    colors =  Color.objects.all()
    user = request.user
    products = Product.objects.all()
    cart = Cart.objects.filter(user=user , ordered=False)
    categories = Category.objects.all()
    filters = Filter.objects.all()
    if cart.exists():
         return render(request,'Store/products.html', {
        "products": products,
        "cart": cart[0],
        "categories" : categories,
        "filters": filters,
        "prices": prices,
        "colors" : colors
        })
    else:
         return render(request,'Store/products.html', {
        "products": products,
        "categories" : categories
        })


def product_detail(request,slug):
    product = get_object_or_404(Product, slug=slug)
    cart = Cart.objects.filter(user=request.user , ordered=False)
    
    if cart.exists():
     return render(request, 'Store/product_detail.html', {
        "product": product,
        "cart": cart[0],
       
     })
    else:
        return render(request, 'Store/product_detail.html', {
        "product": product,
    })




def add_to_cart(request,slug):
    title = "clothes"
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, createdCart = Cart.objects.get_or_create(user=user, ordered=False)
    orderitem, created = Orderitems.objects.get_or_create(user=user, product=product, ordered=False)
    categories = product.categories.filter(title=title)
    if categories.exists():
        category = categories[0]
    else:
        category = ""

    if createdCart and created:
        cart.orderitems.add(orderitem)
        cart.save()
        messages.success(request,'The product was added to your cart')
        return render(request, 'Store/product_detail.html', {
        "product": product,
        "cart": cart,
        "category": category
        })

    elif created:
        cart.orderitems.add(orderitem)
        cart.save()
        messages.success(request,'The product was added to your cart')
        return render(request, 'Store/product_detail.html', {
        "product": product,
        "cart": cart,
        "category": category
        })
        
    else:
        messages.error(request,'The product is already in your cart')
        return render(request, 'Store/product_detail.html', {
        "product": product,
        "cart": cart,
        "category": category
        })

    
def view_cart(request):
    user = request.user
    cart = get_object_or_404(Cart, user=user, ordered=False)
    villes = VilleShipping.objects.all()
    return render(request,'Store/cart.html',{
        "cart":cart,
        "orderitems": cart.orderitems.all(),
        "villes": villes
    })


def update_product_quantity(request,slug):
    user = request.user
    cart = get_object_or_404(Cart, user=user, ordered=False)
    product = get_object_or_404(Product,slug=slug)
    orderitem = Orderitems.objects.get(user=user, product=product, ordered=False)
    villes = VilleShipping.objects.all()

    orderitem.quantity += 1
    if orderitem.quantity >= orderitem.product.stock:
        orderitem.quantity = orderitem.product.stock
    
    orderitem.save()
    #html = '<input id="prod-qte" class="mx-2 border text-center w-12" type="text" value="%s" disabled>' % orderitem.quantity
    #return HttpResponse(html)

    return render(request,'Store/cart.html', {
        "cart":cart,
        "orderitems" : cart.orderitems.all(),
        "villes": villes
    })
 
def remove_product_quantity(request,slug):
     user = request.user
     cart = get_object_or_404(Cart, user=user, ordered=False)
     product = get_object_or_404(Product,slug=slug)
     orderitem = Orderitems.objects.get(user=user, product=product, ordered=False)
     villes = VilleShipping.objects.all()

     if orderitem.quantity == 1:
         orderitem.quantity = 1
     else:
        orderitem.quantity -= 1
    
     orderitem.save()

     return render(request,'Store/cart.html', {
         "cart":cart,
         "orderitems" : cart.orderitems.all(),
         "villes": villes
     })


def remove_orderitem(request,slug):
    user = request.user
    product = get_object_or_404(Product,slug=slug)
    cart = get_object_or_404(Cart, user=user, ordered=False)
    orderitem = Orderitems.objects.get(user=user, product=product, ordered=False)
    villes = VilleShipping.objects.all()
    
    orderitem.delete()    

    return render(request,'Store/cart.html', {
        "cart" : cart,
        "orderitems":cart.orderitems.all(),
        "villes": villes
    })
     
    
    
def checkout(request):
    if request.method == 'POST':
        form = Shipping(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            city = form.cleaned_data['city']
            postal_code = form.cleaned_data['postal_code']
            phone_number = form.cleaned_data['phone_number']
            note = form.cleaned_data['note']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            
            cart = get_object_or_404(Cart, user=request.user, ordered=False)

            msg = first_name + ' ' + last_name + '\n' + 'email :' + email+ '\n'+ address + '\n' + city + ' ' + postal_code + '\n' + phone_number +'\n' + note
            
          #  order = msg + '\n'

          #  for orderitem in cart.orderitems.all():
          #      order += orderitem.product.name + ' quantity : ' + str(orderitem.quantity) + ' total product price: ' + str(orderitem.orderitem_price()) + '\n'
          #      orderitem.ordered = True
          #      orderitem.save()

          #  cart.ordered = True
          #  cart.save()
          #  
          #  send_mail(
          #      'test',
          #      order,
          #      email,
          #      ['youminemyou@gmail.com'],
          #      fail_silently=False  
          #  )
            content = get_template('Store/customer_order.html').render({'orderitems':cart.orderitems.all(), "msg":msg })
            msg = EmailMessage('test',content,email,['youminemyou@gmail.com',email])
            msg.content_subtype = 'html'
            msg.send()
            cart.ordered = True
            cart.save()
            for orderitem in cart.orderitems.all():
                orderitem.ordered = True
                orderitem.save()
            
            user = request.user
            cart, createdCart = Cart.objects.get_or_create(user=user, ordered=False)

            return render(request,'Store/email_sent.html')


    else:
        form = Shipping
        cart = get_object_or_404(Cart, user=request.user, ordered=False)
        return render(request,'Store/checkout.html',{
            "cart":cart,
            "orderitems": cart.orderitems.all(),
            "form": form
            })
