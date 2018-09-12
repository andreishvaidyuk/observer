from django.db import models
from django.contrib.auth.models import User
from datetime import date


# модель Филиала для Организации
class Filial(models.Model):
    name = models.CharField(max_length=20, help_text="Enter a filial name")
    phone = models.CharField(max_length=20, help_text="Enter Phone of Filial")
    address = models.CharField(max_length=20, help_text="Enter Address of Filial")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


# модель Направления в школе (бальные танцы, живопись и тп)
class Section(models.Model):
    name = models.CharField(max_length=20, help_text="Enter a section name")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    filial = models.ForeignKey('Filial', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


# модель Группы в школе (начинающие, дошкольники и тп)
class Group(models.Model):
    name = models.CharField(max_length=20, help_text="Enter a group name")
    filial = models.ForeignKey('Filial', on_delete=models.SET_NULL, null=True, blank=True)
    section = models.ForeignKey('Section', on_delete = models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Ticket(models.Model):
    name = models.CharField(max_length=10, help_text="Enter a ticket name")
    price = models.IntegerField()
    due_date = models.DateField(null=True, blank=True)
    TICKET_TYPE = (
        ('p', 'permanent'),
        ('o', 'one_time'),
    )
    type = models.CharField(max_length=1, choices=TICKET_TYPE, blank=True, default='o', help_text="Choise type of ticket")

    @property
    def is_overdue(self):
        if self.due_date and date.today > self.due_date:
            return True
        return False

    class Meta:
        ordering = ["due_date"]

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=20, help_text="Enter First Name of Student")
    last_name = models.CharField(max_length=20, help_text="Enter Last Name of Student")
    phone = models.CharField(max_length=20, help_text="Enter Phone of Student")
    ticket = models.ForeignKey('Ticket', on_delete = models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    filial = models.ForeignKey('Filial', on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey('Section', on_delete = models.SET_NULL, null=True)
    group = models.ForeignKey('Group', on_delete = models.SET_NULL, null=True)

    class Meta:
        ordering = ["last_name"]

    def __str__(self):
        return '{0}, {1}'.format(self.first_name, self.last_name)