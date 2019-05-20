from django.db import models

class Post(models.Model):
    title = models.CharField() 
    # 찾아보니까 CharField의 속성에 max_length 값을 무조건 설정해줘야 하더라고 그래서 없앴음
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]
