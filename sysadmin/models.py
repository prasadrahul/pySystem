from django.db import models

# Create your models here.
class Logintype(models.Model):
    login_id = models.CharField(max_length=10)
    login_type_name = models.CharField(max_length=30)
    login_type = models.CharField(max_length=40)
    
    def __str__(self):
        return self.login_type_name

class Loginmanagement(models.Model):
    login_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    login_levelid = models.ForeignKey(Logintype)
    login_pwd = models.CharField(max_length=30)
    email = models.EmailField()
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return '%s %s %s' % (self.login_name, self.first_name, self.last_name)

