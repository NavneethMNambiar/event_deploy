from django.db import models

# Create your models here.
class Event(models.Model):
    event_title = models.CharField(max_length=120)
    location = models.CharField(max_length=70)
    date = models.CharField(max_length=120)
    description = models.TextField()
    
    def __str__(self):
        return self.event_title    

class Participant(models.Model):
    participant_name = models.CharField(max_length=60)
    participant_id = models.EmailField(max_length=100)
    participant_phone = models.IntegerField()
    event = models.ForeignKey('Event',on_delete=models.CASCADE)
    def __str__(self):
        return self.participant_name  