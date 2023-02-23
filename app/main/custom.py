from flask_restx import Namespace, fields

parser_ns = Namespace('job_position')
parser = parser_ns.parser()

description_model = parser_ns.model("Description", {
    "description": fields.String( description="The text description"),
})

application_ns = Namespace('application')
application_parser = application_ns.parser()

application_model = application_ns.model("Application", {

    "application": fields.String( description="The text application"),
})
