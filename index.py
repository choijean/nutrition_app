from flask import render_template
from flask.views import MethodView


class Index(MethodView):
    def get(self):
        """
        Delivers HTML for the index (search) page
        """
        return render_template("index.html")
