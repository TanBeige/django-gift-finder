from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import GiftForm
import requests
import json
from constants import HOBBIES, AGE_RANGE, PRICE_RANGE
from demo.models import Product, FormInputs


def home(request):
    # Loads the HTML file base.html

    # Grabs the form model from forms.py and sends it to the base.html template
    form = GiftForm()

    # When someone selects the filters and clicks "submit" This if statement runs
    if request.method == 'GET':


        # Gets the input parameters from the link "?hobby=...age=...price=..."
        hobby = request.GET.get('hobby')
        age = request.GET.get('age')
        price = request.GET.get('price')

        #If no parameters, just return normal
        if hobby == None and age == None and price == None:
            return render(request, "base.html", {'form': form})

        print(hobby, age, price)

        # database_form_entry = FormInputs(category_Hobby=hobby, category_ageRange=age, category_priceRange=price)
        # database_form_entry.save()
        
        print(hobby)
        print(AGE_RANGE[int(age)])
        print(PRICE_RANGE[int(price)])

        # set up the request parameters
        params = {
            'api_key': '7CBC2DADFAC5428BB98CF08115E3F9DC',
            'type': 'search',
            'amazon_domain': 'amazon.com',
            'associate_id': 'gift-finder-django-20',
            'customer_location': 'us',
            'language': 'en_US',
            'output': 'json',
            'sort_by': 'average_review',
            'search_term': hobby,
        }
        # Since we have a limited amount of API usage, I have commented out the get requests
        # If you want API to work, uncomment the lines with 2 #'s

        # Call Rainforest API to get products
        # make the http GET request to Rainforest API
        api_result = requests.get('https://api.rainforestapi.com/request', params)

        # print the JSON response from Rainforest A:PI
        json_results = api_result.json()
        # products = []
        products = json_results['search_results']

        # for product in products:
        #     print(product)
        #     database_product_entry = Product(form_input_id=database_form_entry, giftName=products['title'], giftASIN=products['asin'],
        #                                      giftImageUrl=products['image'], amazonUrl=products['link'])
        #     database_product_entry.save()

        return render(request, "base.html", {'form': form, 'products': products})

    return render(request, "base.html", {'form': form})

