from django.conf import settings
from django.db import models
from django.utils import timezone
# from django import forms

# Create your models here.


class TODO(models.Model):
    title = models.CharField('主題', max_length=100)
    brief = models.CharField('簡述', max_length=300)
    status = models.CharField('狀態', max_length=30)
    doer = models.CharField('數據維護', null=True, blank=True, max_length=100)
    detail = models.TextField('詳情', null=True, blank=True, max_length=1000)
    # date1 = models.DateField('日期',default=timezone.now)
    priority = models.IntegerField('權重', default=0)

    class Meta:
        verbose_name = "TODO"
        verbose_name_plural = "TODO"

    def __str__(self):
        return self.title



class Note(models.Model):
    grp = models.CharField( max_length=100)
    seq = models.IntegerField(default=0)
    title = models.CharField( max_length=300)
    note1 = models.CharField( max_length=300)
    note2 = models.CharField( max_length=300)
    note = models.TextField( default='---')
    
    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Note"

    def __str__(self):
        return self.title


class Index(models.Model):
    owner = models.CharField(default='---',max_length=100)
    app = models.CharField(max_length=100)
    seq = models.IntegerField(default=0)
    link = models.CharField(max_length=300)
    btn = models.CharField(default='btn-info', max_length=300)
    disp = models.CharField(max_length=30)
    note = models.CharField(max_length=100, null=True, blank=True)
    encoder = models.CharField('數據維護人員',max_length=30, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Index主檔"
        verbose_name_plural = "Index主檔"

    def __str__(self):
        return self.app + " " + self.disp


class AppPageAuthGrp(models.Model):
    app = models.CharField(max_length=100)
    page = models.CharField(max_length=100)
    authgrp = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = [['app', 'page']]

        verbose_name = "APP-PAGE-AuthGrp"
        verbose_name_plural = "APP-PAGE-AuthGrp"

    def __str__(self):
        return "|"+self.app+"|"+self.page+"|"+self.authgrp+"|" 


class AppPage(models.Model):
    app = models.CharField(max_length=100)
    page = models.CharField(max_length=100)
    app_name = models.CharField(default='---',max_length=100)
    page_name = models.CharField(default='---',max_length=100)
    title = models.CharField(max_length=100)
    go_up = models.CharField(default="../", max_length=100)

#     grp = models.CharField(max_length=100)
    msg = models.CharField(max_length=100, default='---')
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = [['app', 'page']]

        verbose_name = "頁面主檔"
        verbose_name_plural = "頁面主檔"

    def __str__(self):
        return self.app+" "+self.title


class AppPageMenu(models.Model):
    apppage = models.ForeignKey(
        AppPage, on_delete=models.CASCADE, verbose_name="AppPage")
    seq = models.IntegerField(default=0)
    link = models.CharField(max_length=300)
    btn = models.CharField(default='btn-info', max_length=300)
    disp = models.CharField(max_length=30)
    note = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering =['seq',]
        unique_together = [['apppage', 'disp']]

        verbose_name = "頁面主檔菜單"
        verbose_name_plural = "頁面主檔菜單"

    def __str__(self):
        return self.disp


class AppPageGrp(models.Model):
    apppage = models.ForeignKey(
        AppPage, on_delete=models.CASCADE, verbose_name="AppPage")
    grp = models.CharField(max_length=100)

    def __str__(self):
        return self.grp


class LogAppPage(models.Model):
    app = models.CharField(max_length=100)
    page = models.CharField(max_length=100)
    data = models.CharField(default='---', max_length=300)
    ip = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    agent = models.CharField(max_length=300)
    stamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.page + self.user


class SOP(models.Model):
    name = models.CharField('名稱', max_length=100)
    note = models.CharField(default='---', max_length=300)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "SOP"
        verbose_name_plural = "SOP"

    def __str__(self):
        return self.name


class SOPDetail(models.Model):
    sop = models.ForeignKey(SOP, on_delete=models.CASCADE)
    seq = models.IntegerField(default=0)
    frequency = models.CharField(default='每日', max_length=10)

    title = models.CharField(max_length=100)
    note = models.TextField('備註', null=True, blank=True, max_length=500)

    class Meta:
        ordering = ('seq',)

        verbose_name = "SOP detail"
        verbose_name_plural = "SOP detail"

    def __str__(self):
        return self.title
