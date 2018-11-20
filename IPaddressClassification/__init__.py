#! -*- coding: UTF-8 -*-
__author__ = 'karnikamit'

"""
                                                        IP address classes

Class	1st Octet Decimal Range	| 1st Octet High Order Bits	| Network/Host ID (N=Network, H=Host) |	Default Subnet Mask |	Number of Networks	| Hosts per Network (Usable Addresses)
A	        1 – 126*	            0	                              N.H.H.H	                    255.0.0.0	        126 (27 – 2)	            16,777,214 (224 – 2)
B	        128 – 191	            10	                              N.N.H.H	                    255.255.0.0	        16,382 (214 – 2)	        65,534 (216 – 2)
C	        192 – 223	            110	                              N.N.N.H	                    255.255.255.0	    2,097,150 (221 – 2)	        254 (28 – 2)
D	        224 – 239	            1110	Reserved for Multicasting
E	        240 – 254	            1111	Experimental; used for research
"""