import urllib.parse, urllib.request, urllib.error, json
from flask import Flask, render_template, request
from keys import API_ID, API_KEY

app = Flask(__name__)
# API Info


# recipe finder info
edamam_id = API_ID
edamam_key = API_KEY
edamam_url = "https://api.edamam.com/api/recipes/v2"

def get_recipes(ingredients, cuisine_type=None, health_label=None, max_results=18):
    params = {
        "type": "public",
        "q": ingredients, # query being ingredients
        "app_id": edamam_id,
        "app_key": edamam_key,
        "from": 0,
        "to": min(20, max_results)
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
                hits = data.get("hits", [])[:max_results]
                filtered_recipes = []
                for hit in hits:
                    recipe = hit.get("recipe", {})
                    filtered_recipes.append({
                        "label": recipe.get("label"),
                        "source": recipe.get("url"),
                        "image": recipe.get("image"),
                        "ingredients": recipe.get("ingredientLines")
                    })
                return filtered_recipes
            else:
                print(f"Error: {response.code}")
                return []
    except urllib.error.URLError as e:
        print(f"Request failed: {e}")
        return []




# "label" --> Recipe name
# "image" --> image link
# "ingredientLines" --> list of ingredient lines
# "url" --> link to "martha stewart recipe

@app.route('/')
def index():
    # method GET
    # return homepage
    # render "index.html" template with a form to enter ingredient query, cuisine type (optional), health restrictions, max results
    return render_template('index.html')


@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        try:
            ingredients = request.form.get('query')
            cuisine = request.form.get('cuisine', None)
            health = request.form.get('health label', None)
            max_results = request.form.get('max_results')
            if max_results is None or max_results.strip() == "":
                max_results = 18
            else:
                max_results = int(max_results)

            recipes = get_recipes(ingredients, cuisine, health, max_results)

            # if no recipes --> take to no recipes pages
            if not recipes:
                return render_template('no-results.html')

            return render_template('results.html', recipes=recipes, ingredients=ingredients)
        except Exception as e:
            print(f"Error occurred: {e}")
            return render_template('error.html', message=f"An error occurred: {e}")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)









