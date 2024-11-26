import urllib.parse, urllib.request, urllib.error, json, pprint


# API Info

# farmers market info
farmers_market_key = "pMGafX8SEb"
farmers_market_url = "https://www.usdalocalfoodportal.com/api/farmersmarket/"

# recipe finder info
edamam_id = "1eeca7af"
edamam_key = "68bfe1b3723a03103e9ce043fbd9661c"
edamam_url = "https://api.edamam.com/search"


def get_market_recommendations(zip=98195, radius=10):
    # format paramteres
    # update market url to include keys and parameters
    # gets response as a string
    # loads to json
    # returns market info from given info
    params = {
        "zip": zip,
        "radius": radius,
        "key": farmers_market_key,
    }
    url = f"{farmers_market_url}?{urllib.parse.urlencode(params)}"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            markets = data.get("markets", [])

            # Print each market's name and location
            for market in markets:
                print(f"Market: {market['marketname']}")
                print(f"Address: {market.get('address', 'Not available')}\n")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")

def get_recipes(q, health, cuisineType, max_Results=10):
    # format paramteres
    # update edamam url to include keys, id and parameters
    # gets response as a string
    # loads to json
    # returns recipes from given info
    params = {
        "q": q,
        "app_id": edamam_id,
        "app_key": edamam_key,
        "cuisineType": cuisineType,
        "health": health,
        "to": max_Results
    }

    url = f"{edamam_url}?{urllib.parse.urlencode(params)}"
    # Make the API request

    try:
        with urllib.request.urlopen(url) as response:
            # Read and decode the JSON response
            data = json.loads(response.read().decode())
            recipes = data.get("hits", [])

            # Print each recipe's title and URL
            for recipe in recipes:
                print(f"Recipe: {recipe['recipe']['label']}")
                print(f"URL: {recipe['recipe']['url']}\n")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")

get_recipes("chicken", "gluten-free", "Italian", 10)
















