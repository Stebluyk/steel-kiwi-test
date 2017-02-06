

from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.urls import reverse


class Category(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category:detail", kwargs={"id":self.id})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Category.objects.filter(slug = slug)
    exists = qs.exists()
    if exists:
        new_slug="%s-%s" %(slug,qs.first().id).order_by("-id")
        return create_slug(instance,new_slug = new_slug)
    return slug

def pre_save_field_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug=create_slug(instance)
        instance.save()

pre_save.connect(pre_save_field_slug, sender=Category)    


class Product(models.Model):
 
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product:detail", kwargs={"id":self.id})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug = slug)
    exists = qs.exists()
    if exists:
        new_slug="%s-%s" %(slug,qs.first().id).order_by("-id")
        return create_slug(instance,new_slug = new_slug)
    return slug

def pre_save_field_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug=create_slug(instance)
        instance.save()

pre_save.connect(pre_save_field_slug, sender=Product)    