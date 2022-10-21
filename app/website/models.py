from django.db import models

# Create your models here.

#Must inherit from Django Model class
class Country(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=3)
    region = models.CharField(max_length=30, null=True)
    status = models.CharField(max_length=30, null=True, default='')
    
    def __str__(self):
        return(f'{self.name}')

class Organization(models.Model):
    name = models.CharField(max_length=256)
    image_logo = models.ImageField(upload_to="images", blank=True, null=True)
    short_name = models.CharField(max_length=20, null=True)
    description = models.TextField(null=True)
    category = models.CharField(max_length=50, null=True)
    funded_date = models.DateField(null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    # If you delete a country, his orgs will be also deleted

    def __str__(self):
        return(f'{self.name}')

    def shorten_description(self):
        s = self.description
        if len(s) < 150:
            return s
        else:
            s = s[:150]
            indx = s.rfind(" ")
            s = s[:indx]
            s = s.strip(",") + " ..."
            return s

