from django.db import models
from django.contrib.auth.models import User
from .utils import generate_ref_code


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    code = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='ref_by')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}-{self.code}'

    def get_recommended_profiles(self):
        pass

    def save(self, *args, **kwargs):
        if self.code == '':
            code = generate_ref_code()
            self.code = code
        super().save(*args, **kwargs)