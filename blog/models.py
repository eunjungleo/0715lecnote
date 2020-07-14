from django.db import models

# using Abstract base classes
class CommonInfo(models.Model):
    author = models.CharField(max_length=20) #글쓴이
    body = models.TextField() #본문
    date = models.DateTimeField(auto_now=True) #마지막으로 수정한 날짜
    
    class Meta:
        abstract = True
class Post(CommonInfo):
    title = models.CharField(max_length=100) #제목
    comment = models.ForeignKey('Comment', on_delete=models.DO_NOTHING, related_name='comment_id', default='', blank=True, null=True)
    img = models.ImageField(upload_to='%y/%m/%d', null=True, blank=True)
   
    def __str__(self):
        return self.title

class Comment(CommonInfo):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post_id', default='')



