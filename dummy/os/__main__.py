#!/usr/bin/env python
"""
DummyOS
DummyScript.com
Eric Petersen @Ruckusist <eric.alphagriffin@gmail.com>
"""

__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.1"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Prototype"

""" Launch the docker and start an app... close the app and close
the docker. The program needs to know which dock to use.
"""

import docker
import sys


class DockerControls(object):
    def __init__(self, server_url=None, server_port=None):
        if server_url is None:
            self.client = docker.from_env()
            self.server = "Docker Host: Local Host"
        else:
            self.server = "Docker Host {}:{}".format(server_url, server_port)
            self.client = docker.DockerClient(base_url="tcp://{}:{}".format(
                               server_url, server_port))



    def show_images(self):
        images = self.client.images.list()
        print("Searching {}".format(self.server))
        for image in images:
            name = image.name
            print("Found :: {} ::".format(name))
        
    def run_image(self, image):
        images = self.client.images.list()

        if image in images:
            print("We have the Image we need locally")
            self.client.images.load(image)
            print("The Image is loaded.")

        pass



def main(argz):
    print("Starting Docker Scan")
    dock = DockerControls("agserver", "2375")
    dock.show_images()


if __name__ == '__main__':
    main(sys.argv)
