# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.

class UserDetail(models.Model):
    class Meta:
        db_table = "user_detail"
    gender = models.CharField(max_length=2)
    avatar = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return "{ gender:"+self.gender+"," + \
               " avatar :"+self.avatar + \
               "}"


class User(models.Model):
    class Meta:
        db_table = "user"
    account = models.CharField(max_length=50, null=False, unique=True)
    username = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=100, null=False)
    stat = models.IntegerField(default=0)
    detail = models.OneToOneField(UserDetail, null=True)

    @staticmethod
    def get(**kwargs):
        return User.objects.get(kwargs)


class Plan(models.Model):
    class Meta:
        db_table = 'plan'

    title = models.CharField(max_length=100)
    deadline = models.DateTimeField()
    state = models.IntegerField(default=0)
    create_time = models.DateTimeField()
    content = models.TextField()
    send_notice = models.IntegerField(default=0)
    user = models.ForeignKey(User, null=True)


