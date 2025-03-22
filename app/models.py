from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.email})"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Blog(models.Model):
    image = models.ImageField(upload_to='Blogs/images')
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    content = RichTextField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey('PortfolioCategory', on_delete=models.CASCADE)
    image_1 = models.ImageField(upload_to='Portfolio/images', verbose_name="Pic 1")
    image_2 = models.ImageField(upload_to='Portfolio/images', verbose_name="Pic 2")
    image_3 = models.ImageField(upload_to='Portfolio/images', verbose_name="Pic 3")
    date = models.DateField()
    url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title