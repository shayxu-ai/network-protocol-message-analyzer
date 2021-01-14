#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/01/11 Mon
# @Author: ShayXU
# @Filename: network_protocol_message_analyzer.py


"""
    scapy 20分钟教程 https://github.com/secdev/scapy/blob/master/doc/notebooks/Scapy%20in%2015%20minutes.ipynb?short_path=7cc498d
    Python中Scapy网络嗅探模块的使用 https://www.cnblogs.com/csnd/archive/2004/01/13/11807813.html
    # https://pypi.org/project/scapy/

<<<<<<< HEAD
    # netcat或Hping 也可以考虑

=======
    数据链路层/网络层/传输层/应用层
    Ether()/IP()/TCP()/HTTP()

    # filter 使用的是 Berkeley Packet Filter (BPF)语法
>>>>>>> 1e79a0aea172d3ec005b415f34092f8b47206718
"""


from scapy.all import *


pkt = IP(dst="8.8.8.8")/UDP()/DNS(qd=DNSQR())
# print(repr(raw(pkt)))
# print(pkt.summary())
pkt.canvas_dump()

# ans, unans = traceroute('www.secdev.org', maxttl=15)
# ans.world_trace()
# 这个点很酷，只要知道这些ip归属哪台设备，就可以知道traceroute经过了哪些ip。

# 是否加密(获取设备的密钥)，能不能嗅探