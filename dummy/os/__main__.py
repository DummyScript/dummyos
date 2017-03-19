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
        if server is None:
            self.client = docker.from_env()
        else:
            self.server = "Docker Host {}:{}".format(server_url, server_port)
            self.client = docker.DockerClient(base_url="tcp://{}:{}".fomat(
                               server_url, server_port))



    def show_images(self):
        images = self.client.images.list()
        print("Searching Docker Host: {}")
        for image in images:
            name = image.name
            print("Found :: {} ::".format(name))
        
    def run_image(self, image):
        pass



def main(argz):
    print("Starting Docker Scan")
    dock = DockerControls()

    dock.show_images()


if __name__ == '__main__':
    print("hello world")
    main(0)

    #except Exception as e:
    #    print("exiting dockersuite for {}".format(e))
    #    sys.exit()
