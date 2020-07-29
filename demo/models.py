from django.db import models
# Create your models here.
class FormInputs(models.Model):
    category_Hobby = models.IntegerField()
    category_ageRange = models.IntegerField()
    category_priceRange = models.IntegerField()


class Product(models.Model):

    form_input_id = models.ForeignKey(FormInputs, on_delete=models.CASCADE)
    amazonUrl = models.CharField(max_length=500)
    giftName = models.CharField(max_length=100)
    giftASIN = models.CharField(max_length=10)
    giftDescription = models.CharField(max_length=1000)
    giftImageUrl = models.CharField(max_length=500)
    giftTimestamp = models.DateTimeField(auto_now=True, auto_created=True)
