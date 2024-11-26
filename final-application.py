import urllib.parse, urllib.request, urllib.error, json, pprint
from flask import Flask, render_template, request

app = Flask(__name__)
# API Info

# farmers market info
farmers_market_key = "pMGafX8SEb"
farmers_market_url = "https://www.usdalocalfoodportal.com/api/farmersmarket/"

# recipe finder info
edamam_id = "1eeca7af"
edamam_key = "68bfe1b3723a03103e9ce043fbd9661c"
edamam_url = "https://api.edamam.com/search"

def get_farmers_markets(zip_code, radius):
    parameters = {
        "zip": zip_code,
        "radius": radius,
        "api key": farmers_market_key
    }

    # request farmers market data using GET with parameters
    # if response is valid:
        # return parsed json data with list of farmers markets
    # else:
        #return error message or empty list


def get_recipes(ingredients, cuisine_type, health_label, max_results=10):
    parameters = {
        "q": ingredients,
        "cuisineType": cuisine_type,
        "health": health_label,
        "to": max_results,
        "api_id": edamam_id,
        "api_key": edamam_key
    }

    # request recipe data using GET with parameters
    # if response is valid:
    # return parsed json data with list of recipes
    # else:
    # return error message or empty list


@app.route('/')
def index():
    # method GET
    #return homepage
    # render "index.html" template with a form to enter zip code, radius, recipe query, and preferences


@app.route('/results')
def results():
    # method post
    # retrieve form data
        # zip code and radius for farmers markets
        # query, health, cuisineType, for recipes
    # call get_farmers_markets
    # call get_recipes
    # render "results.html" template
        # list of farmers markets
        # list of recipes




















