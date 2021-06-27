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

    date = models.DateTimeField()
    throughput = models.IntegerField()

    @property
    def logs(self):
        return self.date, self.throughput


class AirportThroughput(models.Model):
    date = models.DateTimeField()
    throughput = models.IntegerField()
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)


class TerminalThroughput(models.Model):
    date = models.DateTimeField()
    throughput = models.IntegerField()
    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)


LAS_TERMINALS = (
    ("Term 1 - AB", "Term 1 - AB"),
    ("Term 1 - C", "Term 1 - C"),
    ("Term 1 - CX", "Term 1 - CX"),
    ("Term 1 - D", "Term 1 - D"),
    ("Terminal 3 - E Lower (1)", "Terminal 3 - E Lower (1)"),
    ("Terminal 3 - E Upper", "Terminal 3 - E Upper"),
)

LAX_TERMINALS = (
    ("Suites", "Suites"),
    ("TBIT Main Checkpoint", "TBIT Main Checkpoint"),
    ("Terminal 1 - Passenger", "Terminal 1 - Passenger"),
    ("Terminal 2 - Passenger", "Terminal 2 - Passenger"),
    ("Terminal 3 - Passenger", "Terminal 3 - Passenger"),
    ("Terminal 4 - FIS", "Terminal 4 - FIS"),
    ("Terminal 4 - Passenger", "Terminal 4 - Passenger"),
    ("Terminal 4a - Passenger", "Terminal 4a - Passenger"),
    ("Terminal 5 - Passenger", "Terminal 5 - Passenger"),
    ("Terminal 5a - Passenger", "Terminal 5a - Passenger"),
    ("Terminal 6 - Passenger", "Terminal 6 - Passenger"),
    ("Terminal 7 - Passenger", "Terminal 7 - Passenger"),
)

MONTHS = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
)

YEARS = (
    ("2020", "2020"),
    ("2019", "2019"),
    ("2018", "2018"),
    ("2017", "2017"),
    ("2016", "2016"),
    ("2015", "2015"),
)


class LAXDay(models.Model):
    terminal = models.CharField(max_length=23, choices=LAX_TERMINALS)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return str(self.id)
