from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name
    
    
