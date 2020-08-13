from django.db import models

class Categories(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=100)
    image = models.ImageField(upload_to = 'images')
    added_date = models.DateTimeField()
    cate = models.ForeignKey(Categories,on_delete=models.CASCADE)
