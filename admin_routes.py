from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint("admin", __name__, description="Admin Functionalities")

@blp.route("/employee")
class EmployeeList(MethodView):
    @blp.response(200, EmployeeSchema(many=True))
    def get(self):
        