from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name='index'),
   
    path('about',views.about,name='about'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.log,name='login'),
    path('search/',views.search,name='search'),
    path('contact',views.contact,name='contact'),
    path('listing',views.listing,name='listing'),
    path('property/',views.property,name='property'),
    path('profile/',views.profile,name='profile'),
    path('vendorss',views.vendors,name='vendors'),
    path('<slug:slug>/',views.product,name='product'),
    path('product/<slug:slug>/',views.detail,name='detail'),
    path('add_to_wishlist',views.add_to_wishlist,name='add_to_wishlist'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('booking/<int:product_id>/',views.booking,name='booking'),
   
]