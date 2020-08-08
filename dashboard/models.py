from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Page(models.Model):
    page_id = models.IntegerField()
    page_name = models.CharField(max_length = 255)
    page_picture = models.TextField()
    page_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.page_name

# class Post(models.Model):
#     post_id = models.CharField(max_length = 255)
#     post_message = models.TextField()
#     post_picture = models.TextField()
#     post_page = models.ForeignKey(Page, on_delete=models.CASCADE)


#     def __str__(self):
#         display = self.post_message.split(' ')[0] + "..."
#         return display

# class Comment(models.Model):
#     comment_message = models.TextField()
#     comment_from = models.CharField(max_length = 255)
#     comment_id = models.CharField(max_length = 255)
#     comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)

#     def __str__(self):
#         display = self.comment_message.split(' ')[0] + "..."
#         return display