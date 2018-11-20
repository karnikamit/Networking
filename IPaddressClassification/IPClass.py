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
        if not octates:
            raise TypeError("ip_address given is not is proper format or empty")

        first_octate = int(octates[0]) if octates[0] else ""
        for ipClass in self.ip_address_classes:
            ip_octate_range = self.ip_address_classes[ipClass]
            if ip_octate_range[0] <= first_octate <= ip_octate_range[1]:
                return ipClass
        else:
            return "Octate not in range"
