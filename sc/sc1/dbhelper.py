from models import Project, Sprint

# Database access methods
def create_project(title, git_link):
    p = Project.objects.create(title=title, git_link=git_link)
    pass

def create_sprint():
    s = Sprint.objects.create(project="Bruce", test_case="Springsteen")
    pass

def query_project():
    return Project.objects.all()