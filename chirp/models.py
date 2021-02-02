from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Chirp(models.Model):
    user        = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    message     = models.CharField(max_length=160)
    created_at  = models.DateTimeField(auto_now_add=True)
    likes       = models.ManyToManyField(get_user_model(), related_name='like')

    def __str__(self):
        return str(self.message)