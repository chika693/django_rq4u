from django import forms
from django.forms import ModelForm
from.models import user_name

class user_name_form(ModelForm):
    class Meta:
        model = user_name
        fields = "__all__"