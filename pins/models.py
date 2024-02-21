from django.db import models

class Pin(models.Model):

    user = models.CharField(max_length=50)
    pinName = models.CharField(max_length=50)
    pinDesc = models.CharField(max_length=500)
    pinLat = models.DecimalField(max_digits=17, decimal_places=15, default = 0.0)
    pinLong = models.DecimalField(max_digits=17, decimal_places=15, default = 0.0)
    

    def __str__(self):
        return 'User: ' + self.user + ', ' + 'Pin Title: '+ self.pinName