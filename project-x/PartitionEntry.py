#!/usr/bin/python
# coding=utf-8

class PartitionEntry(object):

    windowOpenTimeInSeconds = 0
    windowOpenCount = 0
    windowCloseCount = 0

    def __str__(self):
        msg = ""
        msg += "windowOpenTimeInSeconds =  %i\n" % self.windowOpenTimeInSeconds
        msg += "windowOpenCount = %i\n" % self.windowOpenCount
        msg += "windowCloseCount = %i\n" % self.windowCloseCount
        return msg