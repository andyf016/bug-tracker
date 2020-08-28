from django.db import models
from myuser.models import CustomUser
from django.utils import timezone

"""
Title
Time / Date filed
Description
Name of user who filed ticket
Status of ticket (New / In Progress / Done / Invalid)
Name of user assigned to ticket
Name of user who completed the ticket
"""

class Ticket(models.Model):
    STATUSES = (
        ('N', 'New'),
        ('IP', 'In Progress'),
        ('D', 'Done'),
        ('IN', 'Invalid')
    )
    title = models.CharField(max_length=120)
    time_stamp = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_author') # Fix this maybe
    status = models.CharField(max_length=20, null=True, choices=STATUSES, default='N')
    assigned = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL, blank=True, related_name='user_assigned', default=None)      
    finishing = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL, blank=True, related_name='user_finished', default=None)

    def __str__(self):
        return self.title
