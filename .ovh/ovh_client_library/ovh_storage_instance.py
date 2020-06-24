import ovh


def instance_exists(project_id, name):
    client = ovh.Client()
    storage_instances = client.get('/cloud/project/{}/storage'.format(project_id))
    return any(storage_instance for storage_instance in storage_instances if storage_instance.get('name') == name)


def create_instance(project_id, name):
    client = ovh.Client()
    return client.post('/cloud/project/{}/storage'.format(project_id),
                       archive=False,
                       containerName=name,
                       region='UK',
                       )


def make_instance_private(project_id, storage_id):
    client = ovh.Client()
    client.put('/cloud/project/{}/storage/{}'.format(project_id, storage_id), containerType='private')


def make_instance_static(project_id, storage_id):
    client = ovh.Client()
    client.put('/cloud/project/{}/storage/{}'.format(project_id, storage_id), containerType='static')

