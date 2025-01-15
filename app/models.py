from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField(blank=True, default='default.png')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    likes = models.ManyToManyField('auth.User', related_name='likes')
    dislikes = models.ManyToManyField('auth.User', related_name='dislikes')

    def __str__(self):
        return self.title   

    def snippet(self):
        return self.body[:30] + '...'

class Comment(models.Model):
    body = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    date_edited = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    is_edited = models.BooleanField(default=False)

    def __str__(self):
        return self.body
