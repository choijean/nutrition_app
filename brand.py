from flask import render_template
from flask.views import MethodView
import requests
import os


BASE_URL = "https://trackapi.nutritionix.com/v2/search/item?nix_item_id="
header = {"x-app-id": os.environ["NIX_APP_ID"], "x-app-key": os.environ["NIX_API_KEY"]}


class Brand(MethodView):
    def get(self, item_id):
        """
        Delivers HTML for a specific branded item after calling the Nutritionix API.
        """
        results = requests.get(BASE_URL + item_id, headers=header).json()
        return render_template("item.html", item_id=item_id, results=results)