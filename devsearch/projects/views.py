from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'My own portfolio'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'Awesome open source project I am still working on this'
    },
]

def projects(request):
    page = 'projects'
    number = 10
    context = {
        "page": page,
        "number": number,
        "projects": projectsList,
    }
    return render(request, 'projects/projects.html', context=context)

def project(request, pk):
    projectDetails = None
    for project in projectsList:
        if project["id"] == pk:
            projectDetails = project
    
    context = {"project": projectDetails}
    
    return render(request, 'projects/single-project.html', context)
