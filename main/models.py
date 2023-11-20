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
    image = models.ImageField(upload_to='img/')
    detail = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='News'
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    comment = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.comment