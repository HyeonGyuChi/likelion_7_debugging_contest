from django.db import models

class Post(models.Model):
    title = models.CharField() 
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]
