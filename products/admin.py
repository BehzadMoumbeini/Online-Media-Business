from django.contrib import admin
from .models import Category, Product, File

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent', 'title', 'is_enable', 'created_time']
    list_filter = ['is_enable', 'parent']
    search_fields = ['title']
#if we search for some thing the program will look for it in title field.


#since we can have multiple file per product, we should inline File to Product, as follows
#because the File is Foreignkey-ed to Product
class FileInlineAdmin(admin.StackedInline):
    model = File
    fields = ['title', 'file_type', 'file', 'is_enable']
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_enable', 'created_time']
    list_filter = ['is_enable']
    search_fields = ['title']
    filter_horizontal = ['categories'] #with this line you make a new window in front of the "available categories" and will be named "Chosen categories" to select and filter
    inlines = [FileInlineAdmin]
#after running and add file in web browser, the directory "media" will be created which contains all the files (that is why it should be in gitignore)
#with this we just create media (folder and sub folders) and save the files. to see them on the browser we should
