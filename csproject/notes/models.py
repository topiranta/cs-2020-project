from django.db import models

# Create your models here.

class Owner(models.Model):
    nickname = models.CharField(max_length=30)

    def __str__(self):
        return self.nickname


class Note(models.Model):
    note_text = models.CharField(max_length=200)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.note_text