from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

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



# class PortfolioCategory(models.Model):
#     name = models.CharField(max_length=50)
#     def __str__(self):
#         return f"{self.name}"
    
# class Portfolio(models.Model):
#     image = models.ImageField(upload_to='portfolio/images')
#     category = models.ForeignKey(PortfolioCategory,on_delete=models.CASCADE)
#     url = models.URLField(default='https://github.com/asilbek-ismoilov?tab=repositories')
#     date = models.DateField(auto_now=True)
#     title = models.CharField(max_length=70)
#     size = models.CharField(max_length=20, default='col-lg-5')

#     def __str__(self):
#         return f"{self.title} by {self.category}"