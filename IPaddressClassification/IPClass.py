#! -*- coding: UTF-8 -*-
__author__ = 'karnikamit'


class IPClass(object):
    def __init__(self):
        self.ip_address_classes = {
            "A": [1, 126],
            "B": [128, 191],
            "C": [192, 223],
            "D": [224, 239],
            "E": [240, 254]
        }

    def get_class(self, ip_address):
        """
        IP address class is determined by 1st Octet Decimal Range
        :param (str) ip_address: "a.b.c.d"
        :return (str): Class this IP belongs to
        """
        ip_address.strip()
        octates = ip_address.split('.')
        if not octates.__len__() == 4:
            raise TypeError("ip_address given is not in proper format or empty")

        first_octet = int(octates[0]) if octates[0] else ""
        for ipClass in self.ip_address_classes:
            ip_octet_range = self.ip_address_classes[ipClass]
            if ip_octet_range[0] <= first_octet <= ip_octet_range[1]:
                return ipClass
        else:
            return "Octet not in range"
