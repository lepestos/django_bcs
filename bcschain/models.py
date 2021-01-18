from django.db import models


class Block(models.Model):
    height = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=128)
    timestamp = models.DateTimeField()
    address = models.CharField(max_length=128)
    transactions = models.IntegerField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'Height: {self.height}'
