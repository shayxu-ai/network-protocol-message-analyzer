#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/01/11 Mon
# @Author: ShayXU
# @Filename: network_protocol_message_analyzer.py


"""
    scapy 20分钟教程 https://github.com/secdev/scapy/blob/master/doc/notebooks/Scapy%20in%2015%20minutes.ipynb?short_path=7cc498d
    # https://pypi.org/project/scapy/

    # netcat或Hping 也可以考虑

"""


from scapy.all import *
pkt = IP(dst="8.8.8.8")/UDP()/DNS(qd=DNSQR())
# print(repr(raw(pkt)))
# print(pkt.summary())
pkt.canvas_dump()