
from django.utils.text import slugify
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name




class Product(models.Model):
    title = models.CharField(max_length=500 , verbose_name=_('Title'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category') , related_name='categories' ,blank=True, null=True)
    short_description = models.CharField(max_length=100,verbose_name=_('Short Description') , blank=True)
    description = models.TextField(verbose_name=_('Description'))
    price = models.PositiveIntegerField(default=0 , verbose_name=_('Price'))
    active = models.BooleanField(default=True , verbose_name=_('Active'))
    image  = models.ImageField(upload_to='products/product_cover', verbose_name=_('Image') , blank=True)
    slug = models.SlugField(verbose_name=_('Slug') , blank=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            # تولید slug از name
            self.slug = slugify(self.title)
            # حذف خط تیره‌ها
            self.slug = self.slug.replace('-', ' ')
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product-detail' , args=[self.pk])




    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')



class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager , self).get_queryset().filter(active=True)




class Comment(models.Model):
    PRODUCT_STARTS = [
        ('1' , _('Very Bad')),
        ('2' , _('Bad')),
        ('3' , _('Normal')),
        ('4' , _('Good')),
        ('5' , _('Prefect')),

    ]


    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name='comments')
    author = models.ForeignKey(get_user_model() , on_delete=models.CASCADE , related_name='comments' , verbose_name=_('Comment Author'))
    body = models.TextField(verbose_name=_('Comment Text'))
    stars = models.CharField(max_length=10 , choices=PRODUCT_STARTS  , verbose_name=_('Score'))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    # Manager
    object = models.Manager()
    active_comments_manager = ActiveCommentsManager()

    def get_absolute_url(self):
        return reverse('product-detail' , args=[self.product.id])


    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')