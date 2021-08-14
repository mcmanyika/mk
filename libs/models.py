from django.db import models

# Create your models here.


class DeployedTickets(models.Model):
    sponser = models.CharField(max_length=80)
    accountAddress = models.CharField(max_length=80)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def _str_(self):
        return self.accountAddress
