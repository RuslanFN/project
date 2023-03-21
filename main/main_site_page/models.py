from django.db import models

class Class(models.Model):
    subject = models.ForeignKey(subject, on_delete=models.PROTECT)
    teacher = models.ForeignKey(teacher, on_delete=models.PROTECT)
    date = models.DateField()
    time = models.DurationField()
    group = models.ForeignKey(group, on_delete=models.PROTECT)

class teacher(models.Model):
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)

class group(models.Model):
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)

class subject(models.Model):
    name = models.CharField(max_length=20)

class classroom(models.Model):
    name_lesson = models.CharField(max_length=20)
    name_teacher = models.CharField(max_length=20)
    date = models.DateField()
    time = models.DurationField()
