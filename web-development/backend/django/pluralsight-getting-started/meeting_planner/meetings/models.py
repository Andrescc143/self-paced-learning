from datetime import time

from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=300)
    floor = models.IntegerField()
    room_number = models.IntegerField()
    
    def __str__(self):
        return f"The room {self.name} with room number {self.room_number} at the {self.floor} floor. "
    
    
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
