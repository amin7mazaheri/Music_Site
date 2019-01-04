from django.db import models


# Create your models here.
class Artist(models.Model):
    fname = models.CharField(max_length=20, null=True,blank=True)
    lname = models.CharField(max_length=20, null=True,blank=True)
    nick_name = models.CharField(max_length=20, null=True,blank=True)

    def save(self,*args,**kwargs):
        if self.fname or self.nick_name or self.lname:
            super().save(*args,**kwargs)

    def __str__(self):
        if self.fname and self.lname:
            return self.fname+ ' '+self.lname
        elif self.fname:
            return self.fname
        elif self.lname:
            return self.lname
        elif self.nick_name:
            return self.nick_name
        else:
            return ''


class Album(models.Model):
    artist= models.ForeignKey(Artist,on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=20, null=True)
    discription = models.TextField(null=True)
    cover = models.ImageField(null=True,upload_to='albums/%Y-%m-%d/')
    summary = models.CharField(max_length=100, null=True)
    rate = models.FloatField(default=0, null=True)
    like= models.PositiveSmallIntegerField(default=0, null=True)
    released_date = models.DateField(null=True)

    def __str__(self):
        return self.title


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    title= models.CharField(max_length=20)
    music = models.FileField(upload_to='albums/%Y-%m-%d/')

    def __str__(self):
        return self.title


class Tag(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE, null=True)
    title= models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title
