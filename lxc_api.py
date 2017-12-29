import lxc
from bottle import run, request, get, post


@get('/list')
def list():
    container_list = lxc.list_containers()

    return  "List of containers: {0}\n".format(container_list)

@get('/status')
def status():
    containers_states = dict()
    for containers in lxc.list_containers():
        container = lxc.Container(containers)
        container_name = container.name
        container_state = container.state
        containers_states[container_name] = container_state
        for i, j in containers_states():
            

    return  "Containers statuses are: {0}\n".format(containers_states)

run(host='localhost', port='8080', debug=True)
