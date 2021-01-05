from flask import request, render_template
from flask.views import MethodView
import requests
import os


BASE_URL = "https://trackapi.nutritionix.com/v2/natural/nutrients"
header = {"x-app-id": os.environ["NIX_APP_ID"], "x-app-key": os.environ["NIX_API_KEY"]}


class Item(MethodView):
    def post(self):
        """
        Delivers HTML for an item after calling the Nutritionix API.
        """
        item_name = request.form["item_name"]
        body = {"query": item_name}
        results = requests.post(BASE_URL, headers=header, data=body).json()
        return render_template("item.html", item_name=item_name, results=results)