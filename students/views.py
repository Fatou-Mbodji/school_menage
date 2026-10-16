from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenue a ABD - Page d'accueil")

def student_list(request):
    return HttpResponse("Liste des etudiants")

def student_detail(request, id):
    return HttpResponse(f"Detail de l'etudiant {id}")

def about(request):
    return HttpResponse("A propos")

def teacher_list(request):
    return HttpResponse("Liste des profs")

def course_list(request):
    return HttpResponse("Liste des cours")
