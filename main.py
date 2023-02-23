# from flask import Flask, request
# from flask_restx import Resource, Api
# import spacy
# import re
#
# app = Flask(__name__)
# api = Api(app)
#
# nlp = spacy.blank("en")
#
# qualifications = ["BCA", "bca", "Bachelor’s", "BS", "MS", " MCA", "associate"]
# certifications = [
#     "Sun Certified Java Developer",
#     "Sun Certified Java",
#     "Sun Certified",
#     "Certified Java Developer",
#     "Certified Java",
#     "python Certified ",
#     "Security certifications",
#     "Database Administrator certifications",
#     "Hubspot",
#     "SEMrush",
#     "Google ads",
#     "Google analytics",
#     "Social media marketing"
# ]
# skills = ["nlp",
#           "database modeling",
#           "database",
#           "mysql",
#           "node.js",
#           "javascript",
#           "css",
#           "html5",
#           "mpower",
#           "microsoft word",
#           "html",
#           "R",
#           "React",
#           "Angular",
#           "Odoo",
#           "machine learning",
#           "flask",
#           "c++",
#           "design patterns",
#           "sql",
#           "excel",
#           "java",
#           "python",
#           "bootstrap",
#           "word",
#           "Architecture",
#           "analysis",
#           "Databases",
#           "php", "java", "HTML5", "CSS3", "JavaScript", "JQuery", "PostgreSQL", "css", "Bootstrap", "SASS", "Git",
#           "html", "xml", "Python", "html", "javascript", "GWT", "Python", "Perl", "visualization", "jQuery", "JSF",
#           "MVC", "Spring", "COBOL", "SQL", "Java", "JEE", "Software design", "documentation", "testing"]
# stop_words = spacy.lang.en.stop_words.STOP_WORDS
#
#
# @api.route("/extract")
# class Extract(Resource):
#     def get(self):
#         pass
#
#     @api.param("description")
#     def post(self):
#         text = request.args.get("description")
#
#         text = request.json["text"]
#         doc = nlp(text)
#
#         experience_pattern = re.compile(r"(\d+)\s*[-+]\s*(\d+)\s*years", re.IGNORECASE)
#         experience_matches = re.findall(experience_pattern, text)
#
#         if experience_matches:
#             min_exp, max_exp = map(int, experience_matches[0])
#             if min_exp == max_exp:
#                 max_exp = min_exp + 1
#         else:
#             min_exp, max_exp = 0, 1
#
#         extracted_skills = []
#         for token in doc:
#             if token.text in skills and token.text.lower() not in stop_words:
#                 extracted_skills.append(token.text)
#         extracted_qualification = []
#         for qualification in qualifications:
#             if qualification in text:
#                 qualification_doc = nlp(qualification)
#                 filtered_qualification = []
#
#                 for token in qualification_doc:
#                     if not token.is_stop:
#                         filtered_qualification.append(token.text)
#
#                 filtered_qualification = "".join(filtered_qualification)
#                 if filtered_qualification:
#                     extracted_qualification.append(filtered_qualification)
#
#         extracted_certifications = []
#         for certification in certifications:
#             if certification in text:
#                 certification_doc = nlp(certification)
#                 filtered_certification = []
#                 for token in certification_doc:
#                     if not token.is_stop:
#                         filtered_certification.append(token.text)
#                 #                 print(filtered_certification)
#                 filtered_certification = " ".join(filtered_certification)
#                 #         print(filtered_certification)
#                 if filtered_certification:
#                     extracted_certifications.append(filtered_certification)
#
#         extracted = {
#             "experience": (min_exp, max_exp),
#             "skills": extracted_skills,
#             "certifications": extracted_certifications,
#             "qualifications": extracted_qualification
#         }
#
#         return extracted, 200
#
#
# if __name__ == '__main__':
#     app.run(debug=True)