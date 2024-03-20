from django.db import models
from django.utils.timezone import now
class Listing(models.Model):

    class SaleType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'
    
    class HomeType(models.TextChoices):
        HOUSE = 'House'
        CONDO = 'Condo'
        TOWNHOUSE = 'TownHouse'


    realtor = models.EmailField(max_length=255)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    sale_type = models.CharField(max_length=10, choices = SaleType.choices, default=SaleType.FOR_SALE)
    home_type = models.CharField(max_length=10, choices = HomeType.choices, default=HomeType.HOUSE)
    main_photo = models.ImageField(upload_to='listings/')
    photo1 = models.ImageField(upload_to='listings/')
    photo2 = models.ImageField(upload_to='listings/')
    photo3 = models.ImageField(upload_to='listings/')
    is_published = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=now)

    def delete(self):
        self.main_photo.storage.delete(self.main_photo.name)
        self.photo1.storage.delete(self.photo1.name)
        self.photo2.storage.delete(self.photo2.name)
        self.photo3.storage.delete(self.photo3.name)

        super().delete()

    def __str__(self):
        return self.title

