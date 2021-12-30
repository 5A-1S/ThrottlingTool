import docker
import time

class Client:

    def __init__(self):
        self.client = docker.from_env()

    def list_all_containers_ids(self):
        container_list = self.client.containers.list()
        containers = []
        for container in container_list:
            containers.append(container.id)

        return containers

    def list_all_containers_names(self):
        container_list = self.client.containers.list()
        containers = []
        for container in container_list:
            containers.append(container.name)

        return containers

    def get_container_with_id(self, cont_id):

        container_list = self.client.containers.list()
        for container in container_list:
            if container.id == cont_id:
                return container

        return None

    def get_container_with_name(self, name):

        container_list = self.client.containers.list()
        for container in container_list:
            if container.name == name:
                return container

        return None

    def restart_container_with_id(self, cont_id):

        container = self.get_container_with_id(cont_id)
        container.restart()

    def restart_container_with_name(self, name):

        container = self.get_container_with_name(name)
        container.restart()

    def run_command(self, name, command, detach=False):

        container = self.get_container_with_name(name)

        output = container.exec_run(command, privileged=True, detach=detach)

        return output

