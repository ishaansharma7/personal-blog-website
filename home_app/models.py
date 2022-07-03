from django.db import models

# Create your models here.
class PostDetail(models.Model):
    post_title = models.CharField(max_length=256)
    slug = models.SlugField(null=True, unique=True)
    post_id = models.PositiveIntegerField()
    post_auth = models.CharField(max_length=50, default='')
    auth_link = models.URLField(null=True)
    github_link = models.URLField(null=True, blank=True)
    other_link = models.URLField(null=True, blank=True)
    other_link_desc = models.CharField(max_length=256, null=True, blank=True)
    post_desc = models.TextField()
    creation_date = models.DateField()
    post_video = models.URLField(null=True, blank=True)
    post_image = models.ImageField(null=True, blank=True, upload_to='pic')

    def __str__(self):
        return self.post_title
