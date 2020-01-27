from django import forms
from django.core.exceptions import ValidationError
from slugify import slugify

from .models import Tag, Post


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ["title", "slug"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"})
        }

    def clean_slug(self):
        new_slug = slugify(self.cleaned_data["slug"])

        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError("Slug should be unique")

        return new_slug


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", "body", "slug", "tags"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
            "tags": forms.SelectMultiple(attrs={"class": "form-control"})
        }

    def clean_slug(self):
        new_slug = slugify(self.cleaned_data["slug"])

        return new_slug