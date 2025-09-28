from django import forms
from .models import Destination,Photo

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields= ['name','image','desc']
        labels = {
            'name': '📍 Destination Name',
            'image': '🖼️ Upload Image',
            'desc': '📝 Description',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the name of the travel destination'
            }),
            'desc': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Provide a short description of the destination',
                'rows': 3
            }),
        }

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title','image','destination','price','rating','desc','visiting_time']
        labels = {
            'title': '📌 Photo Title',     # Pushpin emoji
            'image': '🖼️ Upload Image',    # Frame picture emoji
            'destination': '✈️ Select destination',  # File folder emoji
            'desc' : '📝 Description',        
            'price' : '💰 Price (in ₹)',
            'visiting_time': '🕒 Visiting Time',
            'rating': '⭐ Rating (1 to 5)',        
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter photo title'
            }),
            'desc': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Provide a short description of the activity',
                'rows': 3
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price in ₹'
            }),
            'visiting_time': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'E.g., 9:00 AM to 6:00 PM'
            }),
        }