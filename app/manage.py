from flask import Flask, Blueprint
from flask_restx import Api

from app.main.controller.simple_parser_controller import parser_ns, application_ns

app = Flask(__name__)
blueprint = Blueprint('Job_parser', __name__, url_prefix='/Job-parser-api/parser/v1/')
api = Api(blueprint, title="Job Parsing", version="1.0", description="A Job Description Parsing")

api.add_namespace(parser_ns)
api.add_namespace(application_ns)

app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(debug=True)
