#!/usr/bin/env python3
#coding:utf-8
import binascii
import sys
from DexItem import DexHeader

class Dexfile:
    def __init__(self):
        super(Dexfile, self).__init__()
        print("init dexfile")
        # self.filePath = filePath
        self.DexHeader = DexHeader()
        self.init_header("/home/user/classes.dex")

    def init_header(self, filePath):
        f = open(filePath, "rb")
        self.DexHeader.file = f
        f.seek(0x0, 0)
        self.DexHeader.magic = binascii.b2a_hex(f.read(8))
        f.seek(0x8, 0)
        self.DexHeader.checksum = binascii.b2a_hex(f.read(4))
        f.seek(0xc, 0)
        self.DexHeader.signature = binascii.b2a_hex(f.read(20))
        f.seek(0x20)
        self.DexHeader.file_size = binascii.b2a_hex(f.read(1))
        f.seek(0x21)
        self.DexHeader.header_size = binascii.b2a_hex(f.read(1))
        f.seek(0x22)
        self.DexHeader.endian_tag = binascii.b2a_hex(f.read(1))
        f.seek(0x23)
        self.DexHeader.link_size = binascii.b2a_hex(f.read(1))
        f.seek(0x24)
        self.DexHeader.link_off = binascii.b2a_hex(f.read(1))
        f.seek(0x25)
        self.DexHeader.map_off = binascii.b2a_hex(f.read(1))
        f.seek(0x26)
        self.DexHeader.string_ids_size = binascii.b2a_hex(f.read(1))
        f.seek(0x27)
        self.DexHeader.string_ids_off = binascii.b2a_hex(f.read(1))
        f.seek(0x28)
        self.DexHeader.type_ids_size = binascii.b2a_hex(f.read(1))
        f.seek(0x29)
        self.DexHeader.type_ids_off = binascii.b2a_hex(f.read(1))
        f.seek(0x2a)
        self.DexHeader.proto_ids_size = binascii.b2a_hex(f.read(1))
        f.seek(0x2b)
        self.DexHeader.proto_ids_off = binascii.b2a_hex(f.read(1))
        print(self.DexHeader.magic)
    
    def 

def main():
    dex = Dexfile()


if __name__ == '__main__':
    main()






