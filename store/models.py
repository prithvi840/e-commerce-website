from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)
    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'Categories' # Specifies how the plural name of the model will spell
        ordering = ('ordering',)

    def __str__(self):
        return self.title

    objects = models.Manager()


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    added_date = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-added_date',)

    objects = models.Manager

    def __str__(self):
        return self.title
