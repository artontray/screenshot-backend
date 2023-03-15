from django.db import models
from django.contrib.auth.models import User
from category.models import Category


class PrivateScreenshot(models.Model):
    """
    private_screenshot model, related to 'owner' and 'category'.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,related_name='private_scrt_count', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_screenshot_ijigqc', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title} - Owner: {self.owner}'

