from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    context={}
    shopee=Product.objects.all()
    print(shopee)
    context['shop']=shopee
    return render(request,'shop/home.html',context)

@login_required
def search(request):
    context={}
    if request.method=='POST':
        Productname=request.POST['productname']
        print(Productname)
        product=Product.objects.filter(product_name__contains=Productname)
        print(product)
        context['product']=product
    return render(request,'shop/search.html',context)



def product_details(request):
    context = {}
    if request.method == 'POST':
        pid = request.POST.get('did')
        products = Product.objects.filter(id = pid)
        context['products'] = products
    return render(request,'shop/product_details.html',context)