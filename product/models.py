from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children' , on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    def __str__(self):
         return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        super().save(*args, **kwargs)


class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Color(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
# Create your models here.
class Product(models.Model):
    category = models.ManyToManyField(Category ,null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products')
    discount = models.IntegerField(default=0)
    size = models.ManyToManyField(Size, blank=True , related_name='products' )
    color = models.ManyToManyField( Color , blank=True, related_name='products' )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.price} - {self.discount}'

class Information(models.Model):
    content = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='informations' ,null=True, blank=True)

    def __str__(self):
        return self.content
