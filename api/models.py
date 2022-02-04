from django.db import models
import string
import random

#generate an unique code for each room
def generate_unique_code():
    length = 6
    
    while True:
        code=''.join(random.choices(string.ascii_uppercase,k=length))
        if Room.objects.filter(code=code).count()==0:
            break
    return code

# Create your models here.

#store informtion for the room
class Room(models.Model):
    code = models.CharField(default=generate_unique_code, max_length=8, unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    # add date and time to the room automatically 
    create_at=models.DateTimeField(auto_now_add=True)
    current_song=models.CharField(max_length=50,null=True)