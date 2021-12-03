from django.shortcuts import render

# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse


def index(request):
    return render(request, 'index.html')

def gemas(request):
    return render(request, 'pages/gemas.html')

def historia(request):
    return render(request, 'pages/historia.html')

def contato(request):
    return render(request, 'pages/contato.html')

def download(request):
    return render(request, 'pages/download.html')

def equipe(request):
    return render(request, 'pages/equipe.html')

def faq(request):
    return render(request, 'pages/faq.html')

def mapas(request):
    return render(request, 'pages/mapas.html')

def personagens(request):
    return render(request, 'pages/personagens.html')

def politica(request):
    return render(request, 'pages/politica-de-privacidade.html')

def base(request):
    return render(request, 'pages/base.html')

def agradecimento(request):
    return render(request, 'pages/agradecimento.html')



def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'Season_Gems.zip'
    # Define the full file path
    filepath = BASE_DIR + '/' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response



