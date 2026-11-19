from django.shortcuts import render
from django.http import Http404

def home(request):
    return render(request, "students/home.html")

def home(request):
    context = {
        "school_name": "Lycée d'Excellence de Dakar",
        "nb_classes": 12,
    }
    return render(request, "students/home.html", context)

# Données temporaires : elles viendront de la base de données plus tard
STUDENTS = [
    {"id": 1, "first_name": "Awa", "last_name": "Diop", "classe": "L2"},
    {"id": 2, "first_name": "Moussa", "last_name": "Fall", "classe": "L2"},
    {"id": 3, "first_name": "Fatou", "last_name": "Ndiaye", "classe": "L2"},
    {"id": 4, "first_name": "Ibrahima", "last_name": "Sow", "classe": "L2"},
    {"id": 5, "first_name": "Anta", "last_name": "Diop", "classe": "L2"},
    {"id": 6, "first_name": "Ibrahim", "last_name": "Sow", "classe": "L2"},
]

def student_list(request):
    context = {"students": STUDENTS}
    return render(request, "students/student_list.html", context)