#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/01/11 Mon
# @Author: ShayXU
# @Filename: network_protocol_message_analyzer.py


"""
    scapy 20分钟教程 https://github.com/secdev/scapy/blob/master/doc/notebooks/Scapy%20in%2015%20minutes.ipynb
    Python中Scapy网络嗅探模块的使用 https://www.cnblogs.com/csnd/archive/2004/01/13/11807813.html
    官方文档 https://pypi.org/project/scapy/

    1、嗅探数据报文
    2、通过定义报文特征，将报文划入不同分组。（未划分的，就可以忽略）
    3、不同分组代表不同的业务流程。
    4、检验业务流程(怎么去验证)

    # 验证方法
    1、Tcp建链过程
    2、Http响应内容
    3、IGMP?
    4、DHCP?


    数据链路层/网络层/传输层/应用层
    Ether()/IP()/TCP()/HTTP()

    # filter 使用的是 Berkeley Packet Filter (BPF)语法
    # netcat或Hping 也可以考虑
"""


from scapy import main
from scapy.all import IP, UDP, DNS, DNSQR, raw, rdpcap


# pkt = IP(dst="8.8.8.8")/UDP()/DNS(qd=DNSQR())
# print(repr(raw(pkt)))
# print(pkt.summary())

# ans, unans = traceroute('www.secdev.org', maxttl=15)
# ans.world_trace()
# 这个点很酷，只要知道这些ip归属哪台设备，就可以知道traceroute经过了哪些ip。

# 是否加密(获取设备的密钥)，能不能嗅探

if __name__ == "__main__":
    filename = "机顶盒开机包.pcapng"
    pcap_p = rdpcap(filename)
