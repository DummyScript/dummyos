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
            # name = image.name
            print("Found :: {} ::".format(image))
        
    def run_image(self, image):
        print("searching locally for {}".format(image))
        images = self.client.images.list()
        print("{}".format(images))
        for x in images:
            name = x.attrs.keys('name')
            print("current tag: {}".format(name))
            if image in name:
                print("We have the Image we need locally")
                self.client.images.load(image)
                print("The Image is loaded.")
        
        else:
            print("We need to download this one... hold")
            search_results = self.client.images.search(image)
            print("{}".format(search_results))
            self.client.images.pull(search_results[0]['name'])
            print("pulled {} and it to docker images".format(image)) 



def main(argz):
    print("Starting Docker Scan")
    # dock = DockerControls("agserver", "2375")
    dock = DockerControls()
    dock.show_images()
    dock.run_image('ruckusist/dummyos:latest')


if __name__ == '__main__':
    main(sys.argv)
