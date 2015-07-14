from django.db import models

# Create your models here.


class Cooperative(models.Model):
    name = models.CharField(max_length=256)
    cuit = models.CharField(max_length=256)
    registration = models.IntegerField()
    address = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class Partner(models.Model):
    cooperative = models.ForeignKey(Cooperative)
    name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    dni = models.IntegerField()
    cuit = models.CharField(max_length=256)
    address = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name + self.last_name


class Withdrawal(models.Model):
    number = models.IntegerField()
    partner = models.ForeignKey(Partner)
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
