from django.db import models
from django.urls import reverse

class GCand(models.Model):
    Gname=models.CharField(max_length=100)
    Ghouse=models.CharField(max_length=50)
    Gpic=models.FileField(null=True,blank=True)
    Gclass=models.CharField(max_length=10)
    Gcount=models.IntegerField()

    def get_url(self):
        return reverse('gshow', kwargs={'id': self.id})


class BCand(models.Model):
    Bname=models.CharField(max_length=100)
    Bhouse = models.CharField(max_length=50)
    Bpic = models.FileField(null=True,blank=True)
    Bclass = models.CharField(max_length=10)
    Bcount = models.IntegerField()

    def get_burl(self):
        return reverse('bretrieve', kwargs={'id': self.id})


class Voter(models.Model):
    Vname=models.CharField(max_length=100)
    Votedone=models.BooleanField(default=False)
    AdmisNo=models.IntegerField()
    Vhouse=models.CharField(max_length=100)
    Vdob=models.DateField()
    Vclass=models.CharField(max_length=10)
    GCand=models.IntegerField(default=0)
    BCand=models.IntegerField(default=0)

    def get_vurl(self):
        return reverse('vretrieve', kwargs={'id': self.id})


class Teacher(models.Model):
    Tname=models.CharField(max_length=100)
    Tid=models.CharField(max_length=15)
    Tpass=models.CharField(max_length=20)


def __str__(self):
    return self.Gname




def get_gurl(self):
    return reverse('gretrieve',kwargs={'id':self.id})

