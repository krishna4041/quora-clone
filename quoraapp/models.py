from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    question_by = models.CharField(max_length=30)
    question_title=models.CharField(max_length=100)

    # def __str__(self):
    #     return self.title


class Answer(models.Model):
    answer_by = models.CharField(max_length=30)
    answer_ans = models.TextField(blank=True, null=True)
    upvote=models.IntegerField(default=0)
    for_flag=models.IntegerField(default=0)
    for_question = models.ForeignKey(Question, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title

class Comment(models.Model):
    comment_by=models.CharField(max_length=30)
    comment_text=models.CharField(max_length=200)
    for_comment=models.ForeignKey(Answer,on_delete=models.CASCADE)

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    answer_id=models.IntegerField(default=0)

# Create your models here.

