# Create your SHOP views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Contact,Order

def index(request):
    # For saving emails to database
    if request.method=="POST":
        print(request)
        email=request.POST.get('email', '')
        contact = Contact(email=email)
        contact.save()
    # For saving emails to database
        
    products= Product.objects.all()
    params={'product': products}
    return render (request,"shop/index.html",params)
	
def aboutus(request):
	return HttpResponse("Shop About Page")
    
def contactus(request):
	return HttpResponse("Shop Contact Us")

def order(request):
    params={}
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('fullname', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        pincode=request.POST.get('pincode', '')
        
        order = Order(items_json= items_json, name=name, email=email, address=address, city=city, state=state, pincode=pincode)
        order.save()
        thank=True
        id=order.order_id
        params={'thank':thank,'id':id}
    return render(request,"shop/order.html",params)
    
def Store(request):
	products= Product.objects.all()
	params={'product': products}
	return render(request,"shop/Store.html",params)
    
def project_info(request):
	return render(request,"shop/project_info.html")

