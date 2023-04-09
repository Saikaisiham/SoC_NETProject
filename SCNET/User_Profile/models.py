import datetime
import json
import requests
from django.db import models
from django.contrib.auth.models import User
from .utils import generate_code
import requests

class perPage(models.Model):
    id_t = models.CharField(max_length=12, blank=True, default=generate_code)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', blank=True)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_city_location(self):
        url = f"https://api-adresse.data.gouv.fr/search/?q={self.city},%20Morocco"
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            if data['features']:
                location = data['features'][0]['geometry']['coordinates']
                return location
        return None

    def age(self):
        today = datetime.date.today()
        age = today.year - self.date_of_birth.year
        if today < datetime.date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

    def tran(self):
        if not self.id_t:
            self.id_t = generate_code()

    def save(self, *args, **kwargs):
        self.tran()
        print(f"id_t: {self.id_t}, user: {self.user}, image: {self.image}, date_of_birth: {self.date_of_birth}, city: {self.city}, bio: {self.bio}")
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.id_t} - {self.city}"

    class Meta:
        ordering = ['-updated', '-created']
