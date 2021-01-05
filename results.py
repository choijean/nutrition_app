from flask import request, render_template
from flask.views import MethodView
import requests
import os


BASE_URL = "https://trackapi.nutritionix.com/v2/search/instant?query="
header = {"x-app-id": os.environ["NIX_APP_ID"], "x-app-key": os.environ["NIX_API_KEY"]}


class Results(MethodView):
    def post(self):
        """
        Delivers HTML for the results page after calling the Nutritionix API.
        """
        searchterm = request.form["searchterm"]
        results = requests.get(BASE_URL + searchterm, headers=header).json()
        return render_template("results.html", searchterm=searchterm, results=results)