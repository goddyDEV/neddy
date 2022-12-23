from django import forms
from .models import *



class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = "__all__"


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"


class TestmonyForm(forms.ModelForm):
    class Meta:
        model = Testmony
        fields = "__all__"


class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = "__all__"


class HeroImageForm(forms.ModelForm):

    class Meta:
        model = HeroImage
        fields = "__all__"
        exclude = {'hero'}




class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedia
        fields = "__all__"


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        exclude = ['received_by', 'status']
        widgets = {
            'date_start': forms.DateInput(format='%m/%d/%Y',
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'}),
            'date_delivery': forms.DateInput(format='%m/%d/%Y',
                                             attrs={'class': 'form-control', 'placeholder': 'Select Start date',
                                                    'type': 'date'})
        }

