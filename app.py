"""
A python/flask app that searches for foods using the Nutritionix API
"""
import flask, os
from index import Index
from results import Results
from item import Item
from brand import Brand
from lost import Lost

app = flask.Flask(__name__)  # creates flask app

app.add_url_rule("/", view_func=Index.as_view("index"), methods=["GET"])

app.add_url_rule("/results", view_func=Results.as_view("results"), methods=["POST"])

app.add_url_rule(
    "/results/details", view_func=Item.as_view("details"), methods=["POST"]
)

app.add_url_rule(
    "/results/brand/<item_id>", view_func=Brand.as_view("brand"), methods=["get"]
)

app.add_url_rule("/<path:path>", view_func=Lost.as_view("lost"), methods=["GET"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
