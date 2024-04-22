from django.db import models
import datetime

class Pin(models.Model):

    #currDate = django.utils.timezone.now

    user = models.CharField(max_length=50)
    pinName = models.CharField(max_length=50)
    pinDesc = models.CharField(max_length=500)
    pinLat = models.DecimalField(max_digits=18, decimal_places=15, default = 0.0)
    pinLong = models.DecimalField(max_digits=18, decimal_places=15, default = 0.0)
    #pinDate = models.DateField(default=datetime.date.today)
    
    #Format Name
    def __str__(self):
        return 'User: ' + self.user + ', ' + 'Pin Title: '+ self.pinName 
