from django.contrib import admin
from .models import Contact,vendor,Category,Product,Relatedimage,Booking

# Register your models here.
class vendorAdmin(admin.ModelAdmin):
    list_display=('username','userid','password')

class categoryAdmin(admin.ModelAdmin):
    list_display=('title','slug','category_image','is_active','is_featured')
    list_editable=('slug','is_active','is_featured')
    list_filter=('is_active','is_featured')
    list_per_page=10
    search_fields=('title','description')
    prepopulated_fields={"slug":("title",)}

class RelatedimagesAdmin(admin.StackedInline):
       model=Relatedimage


class productAdmin(admin.ModelAdmin):
    list_display=('title','slug','product_image','price','is_present')
    list_editable=('slug','is_present')
    list_filter=('is_present','sku') 
    search_fields=('title','short_decription','price','detail_description')
    prepopulated_fields={'slug':('title',)}
    inlines=[RelatedimagesAdmin]
    

class bookingAdmin(admin.ModelAdmin):
    list_display=('product','address','pincode','streetaddress','phonenumber','price')

     



admin.site.register(Contact)
admin.site.register(vendor)
admin.site.register(Category,categoryAdmin)
admin.site.register(Product,productAdmin)
admin.site.register(Booking,bookingAdmin)


