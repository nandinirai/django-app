from django.db import models


class Elevator(models.Model):

    name = models.CharField(max_length=255)
    curr_floor = models.IntegerField()
    direction = models.CharField(max_length=255)
    request_id = models.ManyToManyField("Request")
    is_door_open = models.BooleanField()
    is_available = models.BooleanField()

    def __str__(self):
        return f"Elevator ID: {self.name}"


class Request(models.Model):
    elevator_id = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    floor = models.IntegerField()
    direction = models.CharField(max_length=255)

    def __str__(self):
        return f"Request for {self.elevator_id} to go to floor {self.floor}"
