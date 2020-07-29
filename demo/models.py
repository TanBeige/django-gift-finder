from django.db import models


# Create your models here.
class FormInputs(models.Model):
    category_Hobby = models.CharField(max_length=100)
    category_ageRange = models.IntegerField()
    category_priceRange = models.IntegerField()


class Product(models.Model):
    form_input_id = models.ForeignKey(FormInputs, on_delete=models.CASCADE)
    link = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    asin = models.CharField(max_length=10)
    # giftDescription = models.CharField(max_length=1000)
    image = models.CharField(max_length=500)
    giftTimestamp = models.DateTimeField(auto_now=True, auto_created=True)

    def __iter__(self):
        return {
            self.title,
            self.link,
            self.asin,
            self.image
        }
