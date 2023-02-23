# job_description_parser_flask-api

Job Description Parser API

This API allows users to upload job description files in Doc or PDF format or pass a job description as a JSON object and retrieve the relevant skills, experience, qualifications, and certifications required for the job. It uses the Flask-RestX framework to provide a user-friendly interface for accessing the data.
Getting Started

    Clone the repository to your local machine.
    Install the required dependencies by running the command pip install -r requirements.txt.
    Download the spaCy model by running the command python -m spacy download en_core_web_sm.
    Start the application by running the command python app.py.

The application should now be running on http://localhost:5000/. You can use your browser or an API client such as Postman to interact with the API.
Endpoints
/parser/v1/parse

This endpoint accepts a file upload or a job description as a JSON object and returns the relevant skills, experience, qualifications, and certifications required for the job.
Request Body Parameters

    file: A job description file in Doc or PDF format. Required if the description parameter is not provided.
    description: A string representing the job description. Required if the file parameter is not provided.

Response Format
{
    "experience": [
        3,
        5
    ],
    "skills": [
        "finance",
        "customer service",
        "xml",
        "css",
        "workflow",
        "ui",
        "perl",
        "metrics",
        "translating",
        "1",
        "scripting",
        "human resources",
        "communication",
        "marketing",
        "pto",
        "html",
        "web design",
        "python",
        "digital design",
        "visualization",
        "best practices",
        "version control",
        "jquery",
        "graphic arts",
        "performance testing",
        "javascript",
        "frameworks",
        "plus"
    ],
    "certifications": ["java developer"],
    "qualifications": [
        "Bachelor",
        "associate"
    ]
}
License
project is licensed under the MIT License, which allows users to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    The software is provided "as is", without warranty of any kind, express or implied,
    including but not limited to the warranties of merchantability, fitness for a particular
    purpose and noninfringement.

    In no event shall the authors or copyright holders be liable for any claim,
    damages or other liability, whether in an action of contract, tort or otherwise,
    arising from, out of or in connection with the software or the use or other dealings
    in the software.
