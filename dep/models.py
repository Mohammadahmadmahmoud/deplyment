from django.db import models

# Create your models here.
class Product(models.Model):
    
    
    title=models.CharField(max_length=255)
    slug=models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    date_added=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='uploads/',blank=True,null=True)
    aprroved = models.BooleanField(default=False)
