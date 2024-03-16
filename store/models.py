from django.db import models


class ClothingItem(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    image = models.ImageField(upload_to="clothingItem_img/", verbose_name="iamge", blank=True, null=True)
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Clothing Items"
    
    def __str__(self):
        return self.name
    

class Size(models.Model):
    clothes = models.ManyToManyField(ClothingItem, verbose_name="Clothes")
    size = models.CharField(max_length=100, verbose_name="Size", blank=True, null=True)
    price = models.DecimalField(max_digits=10, verbose_name="Price", decimal_places=2, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Sizes"
        
    def __str__(self):
        return self.size
    

class Fabric(models.Model):
    clothes = models.ManyToManyField(ClothingItem, verbose_name="Clothes")
    name = models.CharField(max_length=255, verbose_name="Name", blank=True, null=True)
    image = models.ImageField(upload_to="fabricImage/", verbose_name="Image", blank=True, null=True)
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price", blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Fabrics"
        
    def __str__(self):
        return self.name
    
    
class AdditionalService(models.Model):
    clothes = models.ManyToManyField(ClothingItem, verbose_name="Clothes")
    name = models.CharField(max_length=100, verbose_name="Name", blank=True, null=True)
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price", blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Additional Services"
        
    def __str__(self):
        return self.name