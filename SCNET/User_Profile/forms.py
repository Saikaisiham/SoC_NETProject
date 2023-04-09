from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import perPage
import requests
import json




class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class PerPage(ModelForm):
    city_choices = []
    with open('static/js/ma.json', 'r', encoding='utf-8') as f:
        cities = json.load(f)
    for city in cities:
        city_choices.append((city['city'], city['city']))
    
    city = forms.ChoiceField(choices=city_choices)

    class Meta:
        model = perPage
        fields = ['image', 'date_of_birth', 'city', 'bio']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.city = self.cleaned_data['city']
        user.bio = self.cleaned_data['bio']
        if commit:
            user.save()
        return user





