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

def get_farmers_markets(zip_code, radius,max_results=5):
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
    request = urllib.request.Request(url)
    try:
        # Send the request and process the response
        with urllib.request.urlopen(request) as response:
            if response.code == 200:
                # Parse JSON data
                data = json.loads(response.read())
                # Assuming the response returns a list of markets under a key, e.g., "markets"
                markets = data.get("data", [])[:max_results]
                return markets
            else:
                print(f"Error: Received status code {response.code}")
                return []
    except urllib.error.URLError as e:
        print(f"Request failed: {e}")
        return []


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
    request = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(request) as response:
            if response.code == 200:
                data = json.loads(response.read())
                # Return the top recipes
                print(data.get("hits", [])[max_results])
                return data.get("hits", [])[:max_results]
            else:
                print(f"Error: {response.code}")
                return []
    except urllib.error.URLError as e:
        print(f"Request failed: {e}")
        return []


print(get_farmers_markets(98105, 5, 2))
#get_recipes("chicken", "Indian", "gluten-free", 3)
#get_recipes("spagetti squash", None, None, 1)


# "label" --> Recipe name
# "image" --> image link
# "ingredientLines" --> list of inf=gredient lines
# "url" --> link to "martha stewart recipe

@app.route('/')
def index():
    # method GET
    #return homepage
    # render "index.html" template with a form to enter zip code, radius, recipe query, and preferences
    return render_template('index.html')


@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        try:
            zip_code = request.form.get('zip code')
            radius = request.form.get('radius')
            ingredients = request.form.get('ingredients')
            cuisine = request.form.get('cuisine')
            health = request.form.get('health label')
            max_results = int(request.form.get('max_results'))

            # parse through ingredients list???
            # ingredients_list = [item.strip() for item in ingredients.split(",")]

            recipes = get_recipes(ingredients, cuisine, health, max_results)
            farmers_markets = get_farmers_markets(zip_code, radius)

            return render_template('results.html', recipes=recipes, farmers_markets=farmers_markets)
        except Exception as e:
            print(f"Error occurred: {e}")
            return render_template('error.html', message=f"An error occurred: {e}")
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

















