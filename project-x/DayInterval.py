#!/usr/bin/python
# coding=utf-8

import time
from datetime import datetime
from Partition import Partition
class DayInterval(object):

    timestamp = 0
    currentDate = None

    numberPartitions = 4
    partitions = []

    """
    returns currents partition of the day:
        [ [00:00 - 05:59], [06:00 - 11:59], [12:00 - 17:59], [18:00 - 23:59] ]
    """
    def getCurrentPartition(self):
        d1 = datetime(datetime.today().year, datetime.today().month, datetime.today().day)
        d2 = datetime.today()
        d3 = d2-d1
        return int(round(d3.seconds / self.fetchDelta()))

    def fetchDelta(self):
        return 60 * 60 * 24 / self.numberPartitions

    def __init__(self, timestamp = 0):
        self.timestamp = timestamp
        self.currentDate = time.strftime("%Y/%m/%d")
        self.initPartitions()

    def initPartitions(self):
        i = 0
        self.partitions = []
        while i < self.numberPartitions:
            self.partitions.append(Partition())
            i+=1

    """
    create new partition if a new day starts
    """
    def resetPartition(self):
        if self.currentDate == time.strftime("%d/%m/%Y"): return # nothing to do
        self.initPartitions()

if __name__ == "__main__":
    d = DayInterval()
    d.getCurrentPartition()