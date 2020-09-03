from django import forms

from plugins.adverts import models


class AdvertForm(forms.ModelForm):
    class Meta:
        model = models.Advert
        fields = (
            'name',
            'image',
            'start_display',
            'end_display',
        )
