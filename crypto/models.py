from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    info = models.CharField(max_length=300)
    full_info = models.TextField()
    created = models.DateField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    url = models.CharField(max_length=350)
    # image = models.ImageField(blank=True, upload_to='uploads/% Y/% m/% d/')
    visible = models.BooleanField(default=True)
    with_deposit = models.BooleanField(default=True)
    def __str__(self):
        return self.title

