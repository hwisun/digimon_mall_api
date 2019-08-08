from django.db import models
from user.models import User

class Generation(models.Model):  # 세대별
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Kinds(models.Model): #종족별
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Attribute(models.Model): # 속성별
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Monster(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/monster_images/', null=True)

    def __str__(self):
        return self.title

class List(models.Model):
    gener = models.ForeignKey(Generation, related_name='monsters', on_delete=models.CASCADE)
    attri = models.ForeignKey(Attribute, related_name='monsters', on_delete=models.CASCADE)
    kind = models.ForeignKey(Kinds, related_name='monsters', on_delete=models.CASCADE)
    prev = models.ForeignKey(Monster, related_name='+', on_delete=models.SET_NULL, blank=True, null=True)
    monster = models.ForeignKey(Monster, related_name='monsters', on_delete=models.CASCADE)
    skill = models.TextField(null=True)
    desc = models.TextField()
    price = models.IntegerField(default=0)


class UserMonster(models.Model):
    user = models.ForeignKey(User, related_name='monsters', on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

