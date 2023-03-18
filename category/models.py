from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Category model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    Category will allow user to create like a folder-like to classify
    private screenshots
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50, default='Main', blank=False)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../category_image_mktm2q', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'


def create_category(sender, instance, created, **kwargs):
    if created:
        Category.objects.create(owner=instance)


post_save.connect(create_category, sender=User)
