from django.db import models
from django.contrib.auth.models import User

# Job application model to store user applications and their details for ease of tracking and management.

class JobApplication(models.Model):

    STATUS_CHOICES = [
        ('wishlist',  'Wishlist'),
        ('applied',   'Applied'),
        ('interview', 'Interview'),
        ('offer',     'Offer'),
        ('rejected',  'Rejected'),
    ]

    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    company      = models.CharField(max_length=255)
    role         = models.CharField(max_length=255)
    location     = models.CharField(max_length=255, blank=True)
    status       = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    applied_date = models.DateField(null=True, blank=True)
    url          = models.URLField(blank=True, help_text="Link to the job posting")
    notes        = models.TextField(blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    # Placeholder field for future Google Sheets integration
    sheet_row_id = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.role} at {self.company} ({self.get_status_display()})"