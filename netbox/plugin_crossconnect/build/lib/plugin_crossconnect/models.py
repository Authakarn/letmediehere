from django.db import models
#from extras.models import ChangeLoggedModel

class plugin_crossconnect(models.Model):
     #customer = models.ForeignKey(to="dcim.Tenants",on_delete=models.DO_NOTHING,)
     customer = models.CharField(max_length=50)
     col2 = models.CharField(max_length=50)

#      def __str__(self):
#         return self.customer

# class plugin_crossconnect(models.Model):
#     name = models.CharField(max_length=50)
#     sound = models.CharField(max_length=50)



# class plugin_crossconnect(models.Model):
#     customer = models.CharField(max_length=50