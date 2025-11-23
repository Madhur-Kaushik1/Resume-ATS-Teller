from django.shortcuts import render
from .models import resume_model
from PyPDF2  import PdfReader
from docx import Document

def fun(request):
    return render(request, 'base.html')


def ats_fun(request):
    file = request.FILES['file']
    resume_model.objects.create(file=file)
    file_var = resume_model.objects.last()
    file_path = file_var.file.path
    extract  = file_path.split('.')[-1].lower()
    txt = ''


    if extract == 'pdf':
        file_reading = PdfReader(file_path)

        for i in file_reading.pages:
            extract_var = i.extract_text()
            txt += extract_var.lower() + ' '



    elif extract == 'docx':
        file_reading = Document(file_path)

        for i in file_reading.paragraphs:
            extract_var = i.text
            txt += extract_var.lower() + ' '

    ats_keywords = [
    # Technical Skills
    "python", "javascript", "java", "c", "c++", "c#", "sql", "html", "css",
    "django", "react", "node.js", "express", "mongodb", "mysql", "postgresql",
    "rest api", "api integration", "git", "github", "version control",
    "bootstrap", "jquery", "json", "xml", "linux", "docker", "kubernetes",
    "cloud", "aws", "azure", "google cloud", "ci/cd", "devops",

    # Web Development
    "frontend development", "backend development", "full stack development",
    "responsive design", "cross-browser compatibility", "ui/ux design",
    "web performance optimization", "mvc", "mvt",
]
    

    matched_words = [i for i in ats_keywords if i in txt]
    ans = len(matched_words) / len(ats_keywords) * 100
    return render(request, 'ats_html.html', {'ans': ans})