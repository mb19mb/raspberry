#!/usr/bin/python
# coding=utf-8

import time
from datetime import datetime
from PartitionEntry import PartitionEntry

class DayInterval(object):
    numberPartitions = 4 # @todo konfigurierbar machen

    timestamp = 0
    currentDate = None
    diDateTime = None

    partitions = []

    def getWindowOpenInterval(self):
        partitionEntry = self.partitions[self.getCurrentPartition()]
        print partitionEntry

    """
    returns currents partition of the day (0,1,2,3):
        [ [00:00 - 05:59], [06:00 - 11:59], [12:00 - 17:59], [18:00 - 23:59] ]
    """
    def getCurrentPartition(self):
        d1 = datetime(self.diDateTime.year, self.diDateTime.month, self.diDateTime.day)
        d3 = self.diDateTime - d1
        return int(round(d3.seconds / self.fetchDelta()))

    """
    """
    def fetchDelta(self):
        return 60 * 60 * 24 / self.numberPartitions

    """
    """
    def initPartitions(self):
        i = 0
        self.partitions = []
        while i < self.numberPartitions:
            self.partitions.append(PartitionEntry())
            i+=1

    """
    create new partition if a new day starts
    """
    def resetPartition(self):
        if self.currentDate == time.strftime("%d/%m/%Y"): return # nothing to do
        self.initPartitions()

    """
    """
    def __init__(self, timestamp=0):
        self.timestamp = timestamp
        self.currentDate = time.strftime("%Y/%m/%d")
        self.diDateTime = datetime(
                    datetime.today().year,
                    datetime.today().month,
                    datetime.today().day,
                    datetime.today().hour,
                    datetime.today().minute,
                    datetime.today().second
        )

        self.initPartitions()


if __name__ == "__main__":
    d = DayInterval()
    #print d.getCurrentPartition()
    d.getWindowOpenInterval()