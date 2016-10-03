#!/usr/bin/python
# coding=utf-8

class Logger(object):

    f = None

    def __init__(self, path = '/tmp/project-x.log'):
        # file pointer
        self.f = open(path, "a+")

    def write(self, msg):
        self.f.write(msg + "\n")

    def __del__(self):
        self.f.close()