from django.db import models


class userdetail(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
   

    def __str__(self):
        return self.username + self.email   

class quizapp(models.Model):
        id=models.AutoField(primary_key=True)
        username=models.CharField(max_length=100)
        language=models.CharField(max_length=100)
        question=models.CharField(max_length=1000)
        opt1=models.CharField(max_length=500)
        opt2=models.CharField(max_length=500)
        opt3=models.CharField(max_length=500)
        opt4=models.CharField(max_length=500)
        ans=models.CharField(max_length=500)

        def __str__(self):
            return self.question

class result(models.Model):
        id=models.AutoField(primary_key=True)
        username=models.CharField(max_length=100)
        language=models.CharField(max_length=200)
        question=models.CharField(max_length=1000)
        user_answer=models.CharField(max_length=500,default=False,null=True)
        date=models.DateField(auto_now_add=True)

        def __str__(self):
            return self.question


