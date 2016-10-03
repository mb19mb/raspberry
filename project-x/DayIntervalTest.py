#!/usr/bin/python
# coding=utf-8

import unittest
from DayInterval import DayInterval

class DayIntervalTest(unittest.TestCase):

    def test_fetchDelta(self):
        d = DayInterval()
        self.assertEqual(d.fetchDelta(), 21600)
        d.numberPartitions = 5
        self.assertEqual(d.fetchDelta(), 17280)
        d.numberPartitions = 6
        self.assertEqual(d.fetchDelta(), 14400)

    def test_initPartitions(self):
        d = DayInterval()
        d.initPartitions()
        self.assertEqual(len(d.partitions), d.numberPartitions)

        d.numberPartitions = 5
        d.initPartitions()
        self.assertEqual(len(d.partitions), d.numberPartitions)

        d.numberPartitions = 0
        d.initPartitions()
        self.assertEqual(len(d.partitions), d.numberPartitions)

    def test_getCurrentPartition(self):
        pass
        #@todo tbc

if __name__ == '__main__':
    unittest.main()