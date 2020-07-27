from django import forms
from constants import HOBBIES, AGE_RANGE, PRICE_RANGE
#
# HOBBIES = [
#     ('gaming', 'Gaming'),
#     ('outdoors', 'Outdoors'),
#     ('pets', 'Pets'),
# ]
# AGE_RANGE = [
#     (0, '0-6 Years Old'),
#     (1, '7-12 Years Old'),
#     (2, '13-15 Years Old'),
#     (3, '17-20 Years Old'),
#     (4, '21-28 Years Old'),
#     (5, '29-35 Years Old'),
#     (6, '36+ Years Old'),
#
# ]
# PRICE_RANGE = [
#     (0, '$'),
#     (1, '$$'),
#     (2, '$$$'),
#     (3, '$$$$'),
# ]

# Create each input for the form, then displays it using {{ form }} in the .html
class GiftForm(forms.Form):
    hobby = forms.CharField(label='Hobby', widget=forms.Select(choices=HOBBIES))
    age = forms.CharField(label='Age Range', widget=forms.Select(choices=AGE_RANGE))
    price = forms.CharField(label='Price', widget=forms.Select(choices=PRICE_RANGE))