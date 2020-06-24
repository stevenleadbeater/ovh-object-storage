import ovh


def get_project(name):
    client = ovh.Client()
    projects = client.get('/cloud/project')
    for project_id in projects:
        project = client.get('/cloud/project/{}'.format(project_id))
        if project.get('description') == name:
            return project_id
    raise LookupError
