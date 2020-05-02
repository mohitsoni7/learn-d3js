from django.db import models
from django.contrib.auth.models import User


PROJECT_STATUS = [
    ('PL', 'Pipeline'),
    ('OG', 'On Going'),
    ('CM', 'Completed'),
]


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='emp')
    codename = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    salary = models.PositiveSmallIntegerField()
    total_experience = models.DecimalField(max_digits=4, decimal_places=2)
    skill = models.PositiveSmallIntegerField()


class Profile(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='profile')
    sec_school = models.CharField(max_length=500)
    sec_score = models.DecimalField(max_digits=4, decimal_places=2)
    srsec_school = models.CharField(max_length=500)
    srsec_score = models.DecimalField(max_digits=4, decimal_places=2)
    grade_school = models.CharField(max_length=500)
    grad_score = models.DecimalField(max_digits=4, decimal_places=2)
    postgrad_school = models.CharField(max_length=500, null=True, blank=True)
    postgrad_score = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    phd_school = models.CharField(max_length=500, null=True, blank=True)
    phd_score = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    postdr_school = models.CharField(max_length=500, null=True, blank=True)
    postdr_score = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)


class Technology(models.Model):
    tech = models.CharField(max_length=100)
    experience = models.DecimalField(max_digits=4, decimal_places=2)


class Project(models.Model):
    name = models.CharField(max_length=500)
    client = models.CharField(max_length=500)
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='projs')
    engineer = models.ManyToManyField(Employee)
    backend = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='bend_projs')
    frontend = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='fend_projs')
    status = models.CharField(max_length=5, choices=PROJECT_STATUS)
    score = models.PositiveSmallIntegerField()


class Project2(models.Model):
    name = models.CharField(max_length=500)
    client = models.CharField(max_length=500)
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='p2projects')
    backend = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='p2bend_projs')
    frontend = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='p2fend_projs')
    status = models.CharField(max_length=5, choices=PROJECT_STATUS)
    score = models.PositiveSmallIntegerField()


class Project2Team(models.Model):
    project = models.ForeignKey(Project2, models.CASCADE)
    eng = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='p2teams')



