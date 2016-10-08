from Relais import Relais

import unittest, time

class RelaisTest(unittest.TestCase):

    def test_pin_preallocation(self):
        r = Relais(10,20)
        self.assertEqual(10, r.pin)
        self.assertEqual(20, r.delay)

    def test_connect(self):
        r = Relais(17)
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