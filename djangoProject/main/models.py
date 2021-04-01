from django.db import models
from django.utils.timezone import now

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = "tbl_users"
        verbose_name = "User"
        verbose_name_plural = "Users"
    name = models.CharField("Username",max_length=100)
    email = models.EmailField("Email",max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        db_table = "  tbl_posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    title = models.CharField("Post title",max_length=100)
    description = models.TextField("Post description",max_length=100)
    content = models.TextField("Post content")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)

    def __str__(self):
        return self.title