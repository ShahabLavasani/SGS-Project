from django.db import models

class coinfo(models.Model):
    contnum = models.CharField(max_length=18)
    sector = models.CharField(max_length=8)
    lastuser = models.CharField(max_length=15)
    billnum = models.CharField(max_length=16)
    size = models.IntegerField()
    entertype = models.CharField(max_length=10)
    carrier = models.CharField(max_length=12)
    floater = models.CharField(max_length=12)
    weight = models.CharField(max_length=6)
    prodcode = models.CharField(max_length=15,primary_key=True)
    takhlie = models.CharField(max_length=10)
    matrooke = models.CharField(max_length=3)
    roozha = models.IntegerField()
    class Meta:
       managed = False
       db_table = 'container'

class things(models.Model):
    contcode= models.CharField(max_length=18,primary_key=True)
    count=models.IntegerField()
    billnum=models.CharField(max_length=20)
    prodname=models.CharField(max_length=30)
    class Meta:
        managed= False
        db_table = 'things'
