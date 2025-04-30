from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Tasks
from.forms import CreateTaskForm, CreateNewProject


# Create your views here.
def index(request):
    title = 'Django Course !!!'
    return  render(request, 'index.html', 
            {
                "titulo" : title
            } )


def about(request):
    return  render(request, 'about.html')


def hello(request, username):
    print(username)
    return  HttpResponse("<h2>Hello World %s </h2>" % username)


def projects(request):
#    proyectos = list(Project.objects.values())
#    return  HttpResponse("<h2>Projects</h2>")
    projects = Project.objects.all()
    return render(request, 'projects/projects.html',
                {
                    'projects': projects    
                })

def tasks(request):
#    task = get_object_or_404(Tasks, id = id) # Digo si el atributo de la clase es igual al parámetro de la función
#    return  HttpResponse("<h2>Tasks %s </h2>" % task.titulo)
    tasks = Tasks.objects.all()
    
    return render(request, 'tasks/tasks.html',
                {
                    'tasks': tasks    
                })
    
def create_task(request):
    """    
    print(request.GET['title'])
    print(request.GET['description'])
    Tasks.objects.create(titulo=request.GET['title'], descripcion=request.GET['description'], project_id=1)

    return render(request, 'create_task.html',
                {
                    'form': CreateTaskForm()
                }) """
    if request.method == "GET":
        return render(request, 'tasks/create_task.html', 
        {
            'form': CreateTaskForm()    
        })
    else:
        Tasks.objects.create(titulo=request.POST['title'], descripcion=request.POST['description'], project_id=1)
        return redirect('tasks')
    
def create_project(request):
    if request.method  == 'GET':
        return render(request, 'projects/create_project.html', 
            {
                'form': CreateNewProject()    
            })
    else:
        # print(request.POST)
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
        """  
            print(project)
            return render(request, 'projects/create_project.html', 
            {
                'form': CreateNewProject()    
            }) 
        """

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Tasks.objects.filter(project_id=id)
    return render(request, 'projects/project_detail.html', 
        {
            'project': project,
            'tasks': tasks
        }
    )