import ovh
import sys

from ovh_client_library.ovh_project import get_project
from ovh_client_library.ovh_storage_instance import instance_exists, create_instance, make_instance_static

if len(sys.argv) != 2:
    print("Usage: %s STORAGE_CONTAINER_NAME" % sys.argv[0])
    sys.exit(1)

storage_container_name = sys.argv[1]

client = ovh.Client()

project_id = get_project('DEVELOPMENT')

if instance_exists(project_id, storage_container_name):
    print('Storage container already exists, exiting')
    exit(0)

result = create_instance(project_id, storage_container_name)
storage_id = result.get('id')

make_instance_static(project_id, storage_id)
print('Created storage with id: {}'.format(storage_id))
