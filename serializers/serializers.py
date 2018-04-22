#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from celery_tasks.models import *


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'title', 'deadline', 'state', 'create_time', 'content', 'send_notice', 'user_id')


class UserSerializer(serializers.ModelSerializer):
    detail = serializers.PrimaryKeyRelatedField(many=False, queryset=UserDetail.objects.get())

    class Meta:
        model = User
        fields = ('id', 'account', 'username', 'detail')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'gender', 'avatar', 'age')