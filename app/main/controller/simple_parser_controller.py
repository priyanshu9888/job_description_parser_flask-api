import os

from flask import request
from flask_restx import Api, Resource
from werkzeug.datastructures import FileStorage
from app.main.custom import parser_ns, application_ns, description_model, application_model
from app.main.custom import parser, application_parser
from app.main.service.simple_job_position_parser_service import parse_job_position,parse_job_position_document
from app.main.service.simple_application_parser_service import parse_application_document, parse_application_text

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
@parser_ns.route("/description/")
class Endpoint(Resource):

    @parser_ns.expect(description_model)
    @parser_ns.doc(parser=parser)
    def post(self):
        json_data = request.get_json()
        text = json_data.get("description")

        return parse_job_position(text)

    @parser_ns.route("/document")
    class FileUploadEndpoint(Resource):
        parser = parser_ns.parser()
        parser.add_argument("file", location="files", type=FileStorage)

        @parser_ns.expect(parser)
        def post(self):
            file = request.files.get("file")
            print(file, "OOO")
            print(file.filename, "PPP")
            filename = file.filename
            file.save(os.path.join(UPLOAD_FOLDER, filename))

            result = parse_job_position_document(file)

            return result, 200


@application_ns.route("/summary/")
class ApplicationEndpoint(Resource):
    @application_ns.expect(application_model)
    @application_ns.doc(parser=application_parser)
    def post(self):
        json_data = request.get_json()

        text = json_data.get("application")

        response = {
            "message": "Data received successfully.",
            "application": text,

        }
        return parse_application_text(text)

    @application_ns.route("/document")
    class ApplicationFileUploadEndpoint(Resource):
        parser = application_ns.parser()
        parser.add_argument("file", location="files", type=FileStorage)

        @application_ns.expect(parser)
        def post(self):
            file = request.files.get("file")
            # file_name = file.filename
            # file.save(file_name)
            result = parse_application_document(file)
            print(file)

            return result, 200

