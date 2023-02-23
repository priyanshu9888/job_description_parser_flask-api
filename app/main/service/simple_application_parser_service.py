# from pyresparser.pyresparser import  ResumeParser


def parse_application_document(file):
    resume_parser = ResumeParser(file)
    data = resume_parser.get_extracted_data()
    print(data)

    skills = data.get('skills', [])
    university = data.get('education', [{}])[0].get('college_name', '')
    email = data.get('email', '')
    number = data.get('phone_number', '')
    name = data.get('name', '')
    school = data.get('education', [{}])[0].get('school_name', '')
    certification = data.get('certifications', [{}])[0].get('title', '')
    total_experience = data.get('total_experience', '')
    response ={
        "skill":skills,
        "university":university,
        "certification":certification,
        "totalexp":total_experience,
        "number":number,
        "name":name,
        "email":email,
        "school":school

    }
    print(response)
    return response



def parse_application_text(text):
    resume_parser = ResumeParser(text=text)
    # Parse the text
    data = resume_parser.get_extracted_data()
    print(data)

    skills = data.get('skills', [])
    university = data.get('education', [{}])[0].get('college_name', '')
    email = data.get('email', '')
    number = data.get('phone_number', '')
    name = data.get('name', '')
    school = data.get('education', [{}])[0].get('school_name', '')
    certification = data.get('certifications', [{}])[0].get('title', '')
    total_experience = data.get('total_experience', '')
    response ={
        "skill":skills,
        "university":university,
        "certification":certification,
        "totalexp":total_experience,
        "number":number,
        "name":name,
        "email":email,
        "school":school

    }
    print(response)
    return response
