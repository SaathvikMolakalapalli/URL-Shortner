# shortener/models.py
from django.db import models
import string, random

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

class URL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, blank=True)
    visits = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            # Generate a random code only if not set
            code = generate_code()
            while URL.objects.filter(short_code=code).exists():
                code = generate_code()
            self.short_code = code
        super().save(*args, **kwargs)

