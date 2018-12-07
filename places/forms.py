# Django
from django import forms
# Project
from .models import Place
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class PlaceForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Place
        exclude = ['timestamp']
