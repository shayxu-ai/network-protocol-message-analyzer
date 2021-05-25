#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/01/20 Wed
# @Author: ShayXU
# @Filename: message_classifier.py


"""
    定义报文分类器
"""

from typing import Protocol
from scapy.all import rdpcap, DHCP, BOOTP, IP, HTTP


"""
    应该有一个对象池子，最后每个对象检测自己是否交互成功，最后按顺序打印。
"""

class message_classifier():
    def __init__(self, final_state=None, client_ip=None, server_ip=None) -> None:
        super().__init__()
        self.state = 0                  # 用于记录协议状态
        self.packets = list()           # 用于记录协议相关报文
        self.coment = list()            # 给每个报文，增加备注
        self.result = False             # 验证结果
        self.final_state = final_state  # 最后应该处于的状态
        self.client_ip = client_ip        # 本地ip
        self.server_ip = server_ip      # 服务器ip

    def dhcp(self, packet):
        """
            dhcp
            bootp: Bootstrap Protocol
            专网和内网 dhcp如何区分: serverip
            为什么专网dhcp 发了2次discover

            dhcp option:
            1 = discover
            2 = offer
            3 = request
            5 = ack

        """
        if packet[DHCP].options[0][-1] == 1 and self.state == 0:
            self.packets.append(packet)
            self.state = 1
        
        if packet[DHCP].options[0][-1] == 2 and self.state == 1:
            if self.server_ip == packet[IP].src:
                self.packets.append(packet)
                self.state = 2
            else:
                self.state = 0
                self.packets = list()
        
        if packet[DHCP].options[0][-1] == 3 and self.state == 2:
            self.packets.append(packet)
            self.state = 3
        
        if packet[DHCP].options[0][-1] == 5 and self.state == 3:
            self.packets.append(packet)
            self.state = 4


    def check_state(self):
        return self.state == self.final_state

    def http(self, packet):

        return


if __name__ == "__main__":
    filename = "机顶盒开机包.pcapng"
    pcap_p = rdpcap(filename)

    dhcp_intranet = message_classifier(4, server_ip='192.168.1.1')
    dhcp_private = message_classifier(4, server_ip='42.103.0.1')
    http = message_classifier()
    for p in pcap_p:
        if BOOTP in p:
            dhcp_intranet.dhcp(p)
            # dhcp_private.dhcp(p)
        if HTTP in p:
            http.http()

    
        




