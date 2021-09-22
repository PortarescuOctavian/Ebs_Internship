from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=250, null=True)
	description = models.TextField(null=True)
	date = models.DateTimeField(null=True)
	price = models.DecimalField(max_digits=10, decimal_places=2,null=True)	
	
	class Meta:
		verbose_name = 'Produs'

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo = models.ImageField(null=True)
    # url = models.URLField()
    
    class Meta:
    	verbose_name = 'Imagine'