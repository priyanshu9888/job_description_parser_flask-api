import base64
import binascii
import json
import os

import spacy
import re
import csv
import requests
from werkzeug.utils import secure_filename

nlp = spacy.blank("en")

import csv

All_skills = []
with open("skill_master.csv") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
        if len(row) > 0:
            All_skills.append(row[0])

cleaned_skills = []
for skill in All_skills:
    cleaned_skill = skill.strip("{}").strip('"').strip(")").strip("(").strip(",").strip()
    if cleaned_skill != "":
        cleaned_skills.append(cleaned_skill)

skills = list(set(cleaned_skills))



certifications=[]
with open("application_certification_map.csv") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        certification_name = row["certification_name"]
        capitalized_certification_name = certification_name.title()
        certifications.append(capitalized_certification_name)


with open("main/qualification.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        qualifications=row


stop_words = spacy.lang.en.stop_words.STOP_WORDS


def parse_job_position( text):

    if text:
        description = text


    doc = nlp(description)

    experience_pattern = re.compile(r"(\d+)\s*[-+]\s*(\d+)\s*years", re.IGNORECASE)
    experience_matches = re.findall(experience_pattern, description)

    if experience_matches:
        min_exp, max_exp = map(int, experience_matches[0])
        if min_exp == max_exp:
            max_exp = min_exp + 1
    else:
        min_exp, max_exp = 0, 1

    extracted_skills = set()
    i = 0
    while i < len(doc) - 1:
        skill = doc[i].text + " " + doc[i + 1].text
        skill = skill.lower()
        skill_words = skill.split()
        if all(word not in stop_words for word in skill_words) and skill in skills:
            extracted_skills.add(skill)
            i += 1
        else:
            single_word = doc[i].text
            single_word = single_word.lower()  # convert to lowercase
            if single_word not in stop_words and single_word in skills:
                extracted_skills.add(single_word)
        i += 1
    extracted_skills = list(extracted_skills)

    extracted_qualification = []
    for qualification in qualifications:
        if qualification in description:
            qualification_doc = nlp(qualification)
            filtered_qualification = []

            for token in qualification_doc:
                if not token.is_stop:
                    filtered_qualification.append(token.text)

            filtered_qualification = "".join(filtered_qualification)
            if filtered_qualification:
                extracted_qualification.append(filtered_qualification)

    extracted_certifications = set()
    for certification in certifications:
        if certification in description:
            certification_doc = nlp(certification)
            filtered_certification = []
            for token in certification_doc:
                if not token.is_stop:
                    filtered_certification.append(token.text)
            filtered_certification = " ".join(filtered_certification)
            if filtered_certification:
                extracted_certifications.add(filtered_certification)

    unique_certifications = list(extracted_certifications)

    extracted = {
        "experience": (min_exp, max_exp),
        "skills": extracted_skills,
        "certifications": unique_certifications,
        "qualifications": extracted_qualification
    }
    print(extracted)
    return extracted

def parse_job_position_document(file):
    filetypes = [".pdf", ".docx", ".doc", ".txt", ".rtf", ".pptx"]
    description = None

    if file:
        filename = file.filename
        file_extension = os.path.splitext(filename)[1].lower()
        if file_extension not in filetypes:
            return error_response("ERROR", "RAS-406", "Invalid file type")
        else:
            if file_extension == ".docx":
                file_content = read_docx_file(file)
            else:
                file_content = file.read()
                file_content = file_content.decode('utf-8', 'ignore')
            description = "Parsed content from file: " + file_content
    else:
        return error_response("ERROR", "RAS-404", "Neither description nor file provided")

    doc = nlp(description)



    # doc = nlp(description)

    experience_pattern = re.compile(r"(\d+)\s*[-+]\s*(\d+)\s*years", re.IGNORECASE)
    experience_matches = re.findall(experience_pattern, description)

    if experience_matches:
        min_exp, max_exp = map(int, experience_matches[0])
        if min_exp == max_exp:
            max_exp = min_exp + 1
    else:
        min_exp, max_exp = 0, 1

    extracted_skills = set()
    i = 0
    while i < len(doc) - 1:
        skill = doc[i].text + " " + doc[i + 1].text
        skill = skill.lower()
        skill_words = skill.split()
        if all(word not in stop_words for word in skill_words) and skill in skills:
            extracted_skills.add(skill)
            i += 1
        else:
            single_word = doc[i].text
            single_word = single_word.lower()  # convert to lowercase
            if single_word not in stop_words and single_word in skills:
                extracted_skills.add(single_word)
        i += 1
    extracted_skills = list(extracted_skills)

    extracted_qualification = []
    for qualification in qualifications:
        if qualification in description:
            qualification_doc = nlp(qualification)
            filtered_qualification = []

            for token in qualification_doc:
                if not token.is_stop:
                    filtered_qualification.append(token.text)

            filtered_qualification = "".join(filtered_qualification)
            if filtered_qualification:
                extracted_qualification.append(filtered_qualification)

    extracted_certifications = set()
    for certification in certifications:
        if certification in description:
            certification_doc = nlp(certification)
            filtered_certification = []
            for token in certification_doc:
                if not token.is_stop:
                    filtered_certification.append(token.text)
            filtered_certification = " ".join(filtered_certification)
            if filtered_certification:
                extracted_certifications.add(filtered_certification)

    unique_certifications = list(extracted_certifications)

    extracted = {
        "experience": (min_exp, max_exp),
        "skills": extracted_skills,
        "certifications": unique_certifications,
        "qualifications": extracted_qualification
    }
    print(extracted)
    return extracted

def error_response(status, error_code, error_message):
    """Response for error"""
    data = {"status": status, "status_code": error_code,
            "message": error_message}
    return data

import docx

def read_docx_file(file_path):
    doc = docx.Document(file_path)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return '\n'.join(text)



