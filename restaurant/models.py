from django.db import models

# Create your models here.
class Booking(models.Model):
    Id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=255)
    no_of_guets = models.IntegerField()
    BookingDate = models.DateTimeField()

    def __str__(self):
        return self.Name
    
class Menu(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()

    def __str__(self):
        return self.Title

    def get_item(self):
        return f"{self.Title}:{self.Price * self.Inventory}"