from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title=models.CharField(max_length=200 )
    image =models.ImageField( upload_to="blogs")
    description=models.TextField(max_length=100)
    is_active =models.BooleanField(default=False)
    is_home=models.BooleanField(default=False)
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)
    categories=models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
