from django.db import models


class Ticket(models.Model):
    def __str__(self):
        return self.body[0:25]

    submitter = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    created_at = models.DateField(auto_now=True)