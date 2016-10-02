import sys
sys.path.append('/root/raspi-sensorkit/project-x/components')

from Relais import Relais

import unittest, time

class RelaisTest(unittest.TestCase):

    def test_pin_preallocation(self):
        r = Relais()
        self.assertEqual(17, r.pin)
        self.assertEqual(5, r.delay)

        r = Relais(10,20)
        self.assertEqual(10, r.pin)
        self.assertEqual(20, r.delay)

    def test_connect(self):
        r = Relais()
        r.connect()
        self.assertEqual(r.hasError, False)  # no errors should be occured
        self.assertEqual(r.isConnectedThrough, False)  # circuit should be unconnected
        del(r)

        time.sleep(1)
        r = Relais(17, 1)
        r.connect()
        self.assertEqual(r.hasError, False)  # no errors should be occured
        self.assertEqual(r.isConnectedThrough, False)  # circuit should be unconnected
        del(r)

        time.sleep(1)
        r = Relais(27, 1)
        r.connect()
        self.assertEqual(r.hasError, False)  # no errors should be occured
        self.assertEqual(r.isConnectedThrough, False)  # circuit should be unconnected
        del (r)

if __name__ == '__main__':
    unittest.main()