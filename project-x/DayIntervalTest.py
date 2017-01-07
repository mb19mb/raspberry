#!/usr/bin/python
# coding=utf-8

import unittest
from datetime import datetime
from DayInterval import DayInterval

class DayIntervalTest(unittest.TestCase):


    def test_fetchDelta(self):
        d = DayInterval()
        self.assertEqual(d.fetchDelta(), 21600)
        d.NUMBER_PARTITIONS = 5
        self.assertEqual(d.fetchDelta(), 17280)
        d.NUMBER_PARTITIONS = 6
        self.assertEqual(d.fetchDelta(), 14400)


    def test_initPartitions(self):
        d = DayInterval()
        d.initPartitions()
        self.assertEqual(len(d.partitions), d.NUMBER_PARTITIONS)

        d.NUMBER_PARTITIONS = 5
        d.initPartitions()
        self.assertEqual(len(d.partitions), d.NUMBER_PARTITIONS)

        d.NUMBER_PARTITIONS = 0
        d.initPartitions()
        self.assertEqual(len(d.partitions), d.NUMBER_PARTITIONS)


    def test_getCurrentPartition(self):
        d = DayInterval()
        d.NUMBER_PARTITIONS = 4
        d.diDateTime = datetime(2000, 10, 10, 5, 59)
        self.assertEqual(d.getCurrentPartition(), 0)

        d.diDateTime = datetime(2000, 10, 10, 11, 59)
        self.assertEqual(d.getCurrentPartition(), 1)

        d.diDateTime = datetime(2000, 10, 10, 17, 59)
        self.assertEqual(d.getCurrentPartition(), 2)

        d.diDateTime = datetime(2000, 10, 10, 23, 59)
        self.assertEqual(d.getCurrentPartition(), 3)

        ### increase number of partitions
        d.NUMBER_PARTITIONS = 6
        d.diDateTime = datetime(2000, 10, 10, 3, 59)
        self.assertEqual(d.getCurrentPartition(), 0)

        d.diDateTime = datetime(2000, 10, 10, 7, 59)
        self.assertEqual(d.getCurrentPartition(), 1)

        d.diDateTime = datetime(2000, 10, 10, 11, 59)
        self.assertEqual(d.getCurrentPartition(), 2)

        d.diDateTime = datetime(2000, 10, 10, 15, 59)
        self.assertEqual(d.getCurrentPartition(), 3)

        d.diDateTime = datetime(2000, 10, 10, 19, 59)
        self.assertEqual(d.getCurrentPartition(), 4)

        d.diDateTime = datetime(2000, 10, 10, 23, 59)
        self.assertEqual(d.getCurrentPartition(), 5)

        ### increase number of partitions
        d.NUMBER_PARTITIONS = 24
        d.diDateTime = datetime(2000, 10, 10, 21, 59)
        self.assertEqual(d.getCurrentPartition(), 21)

if __name__ == '__main__':
    unittest.main()