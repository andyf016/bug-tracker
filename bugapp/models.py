from django.db import models
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

class Ticket(models.model):
    STATUSES = (
        ('N', 'New'),
        ('IP', 'In Progress'),
        ('D', 'Done'),
        ('IN', 'Invalid')
    )
    title = models.CharField(max_length=120)
    time_stamp = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE) # Fix this maybe
    status = models.CharField(max_length=20, null=True, choices=STATUSES, default='N')
    assigned_user = models.TextField()      # fix these maybe
    finishing_user = models.TextField()
