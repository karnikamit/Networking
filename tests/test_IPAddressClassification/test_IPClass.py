#! -*- coding: UTF-8 -*-
__author__ = 'karnikamit'

import unittest
from IPaddressClassification.IPClass import IPClass


class TestIPClass(unittest.TestCase):

    def setUp(self):
        self.ipc = IPClass()
        return self.ipc

    def test_get_class_works(self):
        ip_address = "1.1.1.1"
        assert self.ipc.get_class(ip_address) == 'A'

    def test_get_class_exception_raised(self):
        ip_address = '123'
        with self.assertRaises(TypeError):
            self.ipc.get_class(ip_address)

    def test_get_class_octet_range(self):
        ip_address = "1000.1.1.1"
        self.assertEqual(self.ipc.get_class(ip_address), "Octet not in range")


if __name__ == '__main__':
    unittest.main()
