from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    lastname = models.CharField(max_length=180)
    firstname = models.CharField(max_length=180)
    state = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s' % (self.lastname,self.firstname)