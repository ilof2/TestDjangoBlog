from time import time

from django.db import models
from django.shortcuts import reverse
from slugify import slugify


def gen_slug(s):
    return f"{slugify(s)}-{str(int(time()))}"


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField("Tag", blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("post_detail_url", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("update_post_url", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse("delete_post_url", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date_pub"]


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse("tag_detail_url", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("update_tag_url", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse("delete_tag_url", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
