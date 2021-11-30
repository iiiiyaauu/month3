from django.db import models

# Create your models here.
class BlogPost(models.Model):
    image = models.FileField(upload_to='post_pic/', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    reposts = models.IntegerField(default=0)

    def __str__(self):
        return self.title[:15]


