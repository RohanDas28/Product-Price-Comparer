from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Order
from math import ceil



def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    allProds=[]
    catprods = Product.objects.values('category','id')
    cats  = { item['category'] for item in catprods}
    for cat in cats:
        prod=  Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
        
    # allProds = [[products, range(1,nSlides),nSlides],[products, range(1,nSlides),nSlides]]
    # params = {"allProds":allProds}
    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    params= {'allProds':allProds}
    return render(request, 'shop/index.html', params)





