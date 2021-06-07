from django.db import models


class MainMenu(models.Model):
    item = models.CharField(max_length=200, unique=True)
    link = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.item

class Airport(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=3, unique=True)


class Terminal(models.Model):
    name = models.CharField(max_length=200, unique=True)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)


class Throughput(models.Model):

    date = models.DateField()
    throughput = models.IntegerField()

    @property
    def logs(self):
        return self.date, self.throughput


class AirportThroughput(models.Model):
    date = models.DateField()
    throughput = models.IntegerField()
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)


class TerminalThroughput(models.Model):
    date = models.DateField()
    throughput = models.IntegerField()
    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)

