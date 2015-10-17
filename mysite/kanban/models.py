from django.db import models

# Create your models here.


class Board(models.Model):
    order_num = models.IntegerField(default='1')
    title = models.TextField(null=False, blank=False, help_text='title')
    master_user = models.CharField(max_length=100, blank=True,
                                    help_text='user')
    group_user = models.CharField(max_length=100, blank=True,
                                    help_text='group')
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)


class List(models.Model):
    order_num = models.IntegerField(default='1')
    title = models.TextField(null=False, blank=False, help_text='title')
    master_user = models.CharField(max_length=100, blank=True,
                                    help_text='user')
    group_user = models.CharField(max_length=100, blank=True,
                                    help_text='group')
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    board_id = models.ForeignKey(Board)


class Card(models.Model):
    order_num = models.IntegerField(default='1')
    title = models.TextField(null=False, blank=False, help_text='title')
    info = models.TextField(blank=True, help_text='info')
    tag = models.CharField(max_length=100, blank=True,
                            help_text='tag')
    master_user = models.CharField(max_length=100, blank=True,
                                    help_text='user')
    group_user = models.CharField(max_length=100, blank=True,
                                    help_text='group')
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    list_id = models.ForeignKey(List)
