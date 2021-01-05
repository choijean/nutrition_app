from flask import render_template
from flask.views import MethodView


class Lost(MethodView):
    def get(self, path):
        """
        Delivers HTML for the "are you lost" page
        """
        return render_template("lost.html")