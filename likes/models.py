from django.db import models
from django.contrib.auth.models import User
from public_screenshots.models import PublicScreenshot


class Like(models.Model):
    """
    Like model, related to owner and PublicScreenshot
    owner is a User instance and PublicScreenshot is a PublicScreenshot instance.
    unique_together makes sure a user can't like the same PublicScreenshot twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    public_screenshot = models.ForeignKey(
        PublicScreenshot, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'public_screenshot']

    def __str__(self):
        return f'{self.owner} {self.PublicScreenshot}'