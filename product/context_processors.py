from .models import Category
# from django.db.models import Q



def navbar_categories(request):
        categories = Category.objects.all()
        return {'navbar_categories': categories}