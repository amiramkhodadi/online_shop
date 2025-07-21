from django.db import models



class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Information(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content[:20]

class Color(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products')
    discount = models.IntegerField(default=0)
    size = models.ManyToManyField(Size,null=True , blank=True , related_name='products' )
    color = models.ManyToManyField( Color ,null=True , blank=True, related_name='products' )
    created_at = models.DateTimeField(auto_now_add=True)
    information = models.ManyToManyField(Information,null=True , blank=True , related_name='products' )

    def __str__(self):
        return f'{self.title} - {self.price} - {self.discount}'

