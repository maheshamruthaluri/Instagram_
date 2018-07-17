from django.db import models
from django.utils import timezone


class User(models.Model):
    uid = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, null=True)
    age = models.IntegerField(null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50, null=True)
    bio = models.TextField(null=True)
    profile_picture = models.ImageField(null=True)
    join_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Picture(models.Model):
    pid = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    post_picture = models.ImageField(null=True)
    published_date = models.DateTimeField(default=timezone.now)
    #
    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.description


class Like(models.Model):
    lid = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)


class Comment(models.Model):
    cid = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text


