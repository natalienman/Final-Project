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
edamam_url = "https://api.edamam.com/api/recipes/v2"

def get_farmers_markets(zip_code, radius):
    # new_url = farmers_market_url + "?apikey=" + farmers_market_key
    parameters = {
        "apikey" : farmers_market_key,
        "zip": zip_code,
        "radius": radius
    }

    # request farmers market data using GET with parameters
    # if response is valid:
        # return parsed json data with list of farmers markets
    # else:
        #return error message or empty list
    url = f"{farmers_market_url}?{urllib.parse.urlencode(parameters)}"
    print(url)
    # try:
    #     with urllib.request.urlopen(url) as response:
    #         data = json.loads(response.read().decode())
    #         market_data = data.get("data")
    #         if market_data != None:
    #             print(f"No Markets Found")
    #         else:
    #             market_list = {}
    #             for market in market_data:
    #                 if market["directory_type"] == "farmersmarket":
    #                     market_list.









def get_recipes(ingredients, cuisine_type=None, health_label=None, max_results=10):
    params = {
        "type": "public",
        "q": ingredients, # query being ingredients
        "app_id": edamam_id,
        "app_key": edamam_key,
        "from": 0,
        "to": max_results
    }
    if health_label:
        params["health"] = health_label
    if cuisine_type:
        params["cuisineType"] = cuisine_type

    url = f"{edamam_url}?{urllib.parse.urlencode(params)}"
    headers = {
        "Edamam-Account-User": "nenman"
    }
    req = urllib.request.Request(url, headers=headers)

    try:
        # Make the request
        with urllib.request.urlopen(req) as response:
            # Parse the JSON response
            data = json.load(response)
            hits = data['hits'][:max_results]  # Take only the first 'max_results' hits
            print(json.dumps(hits, indent=2))
    except urllib.error.HTTPError as e:
        print(f"HTTPError: {e.code} - {e.reason}")
        print(e.read().decode())  # Additional error details
    except urllib.error.URLError as e:
        print(f"URLError: {e.reason}")


    # request recipe data using GET with parameters
    # if response is valid:
    # return parsed json data with list of recipes
    # else:
    # return error message or empty list



get_farmers_markets(98105, 5)
#get_recipes("chicken", "Indian", "gluten-free", 3)
get_recipes("spagetti squash", None, None, 1)


# "label" --> Recipe name
# "image" --> image link
# "ingredientLines" --> list of inf=gredient lines
# "url" --> link to "martha stewart recipe

@app.route('/')
def index():
    # method GET
    #return homepage
    # render "index.html" template with a form to enter zip code, radius, recipe query, and preferences


@app.route('/results')
def results():
#     method post
#     retrieve form data
#         zip code and radius for farmers markets
#         query, health, cuisineType, for recipes
#     call get_farmers_markets
#     call get_recipes
#     render "results.html" template
#         list of farmers markets
#         list of recipes














