from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import GiftForm
import requests
import json
from constants import HOBBIES, AGE_RANGE, PRICE_RANGE
from demo.models import Product, FormInputs
import sqlite3


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

        # If no parameters, just return normal homepage w/ last 30 recorded products
        if (hobby is None and age is None and price is None) or (hobby == 'none' and age == '0' and price == '0'):
            # Grabs the last 30 products in Products table
            all = Product.objects.order_by('-id')[:30]
            products = all

            # Displays products on homepage
            return render(request, "base.html", {'form': form, 'products': products})

        database_form_entry = FormInputs(category_Hobby=hobby, category_ageRange=age, category_priceRange=price)
        database_form_entry.save()


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
            # Age range grabs pair from list, then grabs value from pair ([1])
            'search_term': f"{hobby} {AGE_RANGE[int(age)][1]}"
        }

        # Call Rainforest API to get products
        # make the http GET request to Rainforest API
        api_result = requests.get('https://api.rainforestapi.com/request', params)

        # print the JSON response from Rainforest A:PI
        json_results = api_result.json()
        products = json_results['search_results']
        # print(database_form_entry)
        for product in products:
            # print(product)
            database_product_entry = Product(form_input_id=database_form_entry, title=product['title'], asin=product['asin'],
                                             image=product['image'], link=product['link'])
            database_product_entry.save()

        return render(request, "base.html", {'form': form, 'products': products})

    return render(request, "base.html", {'form': form})
