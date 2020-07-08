from django import forms
from .models import Contact
from .models import Notes


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
            'birthday',
        ]

        widgets = {
        'birthday': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type':'date'}),
      }


# from django import forms
# from django.forms import ModelForm

# from .models import Promise


# class DateInput(forms.DateInput):
#     input_type = 'date'


# class PromiseForm(ModelForm):

#     class Meta:
#         model = Promise
#         fields = ['title', 'description', 'made_on']
#         widgets = {
#             'made_on': DateInput(),
#         }