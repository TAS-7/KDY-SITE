from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length = 100,null=True)
	subject = models.CharField(max_length = 100)
	question = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete= models.CASCADE)


	def __str__(self):
		return self.subject






class Comment(models.Model):
    question = models.ForeignKey('website.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    answer = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    approved_answer = models.BooleanField(default=False)

    def approve(self):
        self.approved_answer = True
        self.save()

    def __str__(self):
        return self.answer


	
	

