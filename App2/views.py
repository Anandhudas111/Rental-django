from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import SignupForm,SigninForm,ProductForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Contact,vendor,Category,Product,Relatedimage,Wishlist,Booking
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q

# Create your views here.
def index(request):
    categories=Category.objects.filter(is_active=True,is_featured=True)[:3]
    products=Product.objects.filter(is_present=True)[:6]
    context={
        'categories':categories,
        'products':products
    }
    return render(request,'index.html',context)
def registration(request):
    if request.method=='POST':
       form=SignupForm(request.POST)
       if form.is_valid():
           user=form.save(commit=False)
           user.save()
           messages.info(request,'user saved succesfully')
           return redirect('login')
       else:
           messages.info(request,'invalid')
    else:
        form=SignupForm()
    context = { 
            'form':form
    }

    return render(request,'Registration.html',context)
def log(request):
    if request.method=='POST':
        form=SigninForm(request.POST)
        username=form['username'].value()
        password=form['password'].value()
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,'login success')
            return redirect('index')
        else:
            messages.info(request,'invalid')
    else:
        form=SigninForm
    context = {
        'form':form
    }
    return render(request,'login.html',context)
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=='POST':
        email=request.POST['email']
        msg=request.POST['msg']
        Contact(email=email,message=msg).save()
        send_mail(subject='thank you',message='thank you for using website',from_email=settings.EMAIL_HOST_USER,recipient_list=[email,],
                  fail_silently=False)
        messages.info(request,'invalid email')
    return render(request,'contact.html')

def listing(request):
    categories=Category.objects.filter(is_active=True)
    return render(request,'listing.html',{'categories':categories})

def property(request):
    if request.method=='POST':
       
       username=request.POST['username']
       userid=request.POST['userid']
       password=request.POST['password']
       vendordetails=vendor.objects.get(username=username,userid=userid,password=password)
       request.session['username']=vendordetails.username
       if vendordetails:
           return redirect('vendors')
       
   
    return render(request,'property-single.html')

def vendors(request):
    context={}
    form=ProductForm(request.POST or None,request.FILES or None)
    if form.is_valid():  
        form.save()
    context['form']=form

          
    return render(request,'vendorss.html',context)

def product(request,slug):
    category=get_object_or_404(Category,slug=slug)
    products=Product.objects.filter(is_present=True,category=category)

    categories=Category.objects.filter(is_active=True)
    context = {
        'category':category,
        'products':products,
        'categories':categories
    }
    return render(request,'product.html',context)

def detail(request,slug):
    product=get_object_or_404(Product,slug=slug)
    # relatedimages=Relatedimage.objects.filter(products=product.id)
    context={
         'product':product,
        #  'relatedimages':relatedimages,
    }
    return render(request,'detail.html',context)
@login_required
def add_to_wishlist(request):
    user=request.user
    print(request.user)
    product_id=request.GET.get('prod_id')
    product=get_object_or_404(Product,id=product_id)

    item_already_in_wishlist=Wishlist.objects.filter(product=product_id,user=user)
    if item_already_in_wishlist:
        cp=get_object_or_404(Wishlist,product=product_id,user=user)
        cp.save()
    else:
        Wishlist(user=user,product=product).save()
    return redirect('wishlist')
@login_required
def wishlist(request):
    user=request.user
    wish_pro=Wishlist.objects.filter(user=user)
    context={
        'wish_pro':wish_pro,
    }
    return render(request,'wishlist.html',context)



@login_required
def booking(request,product_id):
    if request.method=='POST':
        product=Product.objects.get(id=product_id)
       
        address=request.POST['address']
        streetaddress=request.POST['streetaddress']
        pincode=request.POST['pincode']
        phonenumber=request.POST['phonenumber']
        country=request.POST['country']
        price=request.POST['price']
        Booking(address=address,streetaddress=streetaddress,pincode=pincode,country=country,phonenumber=phonenumber,product=product,price=price).save()
        messages.info(request,'booked sucessfully')
        return render(request,'booking.html')
    return render(request,'booking.html')



def search(request):
    q=request.GET.get('q','')
    data=Product.objects.filter(title__icontains=q).order_by('-id')
    return render(request,'search.html',{'data':data})

@login_required
def profile(request):
    data=request.session['username']
    Book=Booking.objects.all()
    context={
        'data':data,
        'Book':Book
    }
    return render(request,'profile.html',context)