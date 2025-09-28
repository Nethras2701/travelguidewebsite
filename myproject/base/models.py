from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to='destinations/') #upload_to : create one folder and all photos will be stored their
    desc = models.CharField(max_length=1000)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
STAR_CHOICES = [
    (1, '⭐'),
    (2, '⭐⭐'),
    (3, '⭐⭐⭐'),
    (4, '⭐⭐⭐⭐'),
    (5, '⭐⭐⭐⭐⭐'),
]    
class Photo(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='photos/') #upload_to : create one folder and all photos will be stored their
    price = models.PositiveIntegerField()
    desc=models.CharField(max_length=1000)
    visiting_time = models.CharField(max_length=100)
    rating = models.IntegerField(choices=STAR_CHOICES, default=3)
    destination = models.ForeignKey(Destination,on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title