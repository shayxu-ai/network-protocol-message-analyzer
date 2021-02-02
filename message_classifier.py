#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/01/20 Wed
# @Author: ShayXU
# @Filename: message_classifier.py


"""
    定义报文分类器
"""

from typing import Protocol
from scapy.all import DHCP


"""
    最后呢，应该有一个对象池子，最后每个对象检测自己是否交互成功，最后按顺序打印。
"""

class message_classifier():
    def __init__(self, max_state) -> None:
        super().__init__()
        self.state = 0              # 用于记录协议状态
        self.packets = list()        # 用于记录协议相关报文
        self.coment = list()        # 给每个报文，增加备注
        self.result = False
        self.max_state = max_state

    def dhcp(self, packet):
        self.packets.append(packet)
        if packet[DHCP].options[0][-1] == 1:
            
            pass
    








        




