from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    cat_img=models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.title
    
class News(models.Model):
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    detail = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='News'
    
    def __str__(self):
        return self.title