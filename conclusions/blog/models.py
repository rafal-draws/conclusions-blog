from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import activate

STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)

class PlPost(models.Model):
    title = models.CharField(max_length = 200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='pl_blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        activate('pl')
    

class EnPost(models.Model):
    title = models.CharField(max_length = 200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='en_blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        activate('en')