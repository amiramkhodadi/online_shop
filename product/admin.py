from django.contrib import admin

from product.models import Product, Size, Color, Information, Category


# Register your models here.
# admin.site.register(Product)

# admin.site.register(Information)


class InformationAdmin(admin.StackedInline):
    model = Information

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title' , 'price')
    inlines = [InformationAdmin]



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Size)
admin.site.register(Color)