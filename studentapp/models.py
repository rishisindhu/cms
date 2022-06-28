from django.db import 

# Create your models here.

class studentdetails(models.Model):
    roll no = models.IntegerField()
    name = models.charField(max_lengh=50, null=True)
    marks = models.IntegerField()


class studentdetails(models.Model):
    roll no = models.IntegerField()
    name = models.charField(max_lengh=50, null=True)
    marks = models.IntegerField()
