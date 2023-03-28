from django.contrib import admin 
from .models import Book, Review, BookContributor,Publisher
# Register your models here.


class Project1AdminSite(admin.AdminSite):
    title_header = 'Bookr Admin'
    site_header = 'Bookr administration'
    index_title = 'Bookr site admin'

class BookAdmin(admin.ModelAdmin):
    list_display=['title', 'isbn', 'publisher']
    list_filter=['publisher']
    
admin_site=Project1AdminSite(name="Bookr")

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(BookContributor)
admin.site.register(Publisher)
