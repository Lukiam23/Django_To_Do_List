from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=200)
	birthday = models.DateField()
	email = models.EmailField()
	
class ListItem(models.Model):
	name = models.CharField(max_length=200)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)

