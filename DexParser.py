#!/usr/bin/env python3
#coding:utf-8
import binascii
import sys
from DexItem import *

class Dexfile:
    def __init__(self, filePath):
        super(Dexfile, self).__init__()
        print("init dexfile")
        self.filePath = filePath
        self.DexHeader = DexHeader()
        self.DexStringIds        = []
        self.DexTypeIds          = []
        self.DexFieldIds         = []
        self.DexMethodIds        = []
        self.DexProtoIds         = []
        self.DexClassDef         = []

        self.init_header()
        self.init_stringids()




    def init_header(self):

        
        f = open(self.filePath, "rb")
        self.DexHeader.f = f
        f.seek(0x0, 0)
        self.DexHeader.magic = binascii.b2a_hex(f.read(8))
        f.seek(0x8, 0)
        #binary data -> reverse -> Hexadecimal data -> Hexadecimal string  -> Hexadecimal
        self.DexHeader.checksum = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode('utf-8')
        f.seek(0xc, 0)
        self.DexHeader.signature = binascii.b2a_hex(f.read(20))

        f.seek(0x20, 0)
        self.DexHeader.file_size = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode('utf-8')

        f.seek(0x24, 0)
        self.DexHeader.header_size = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode('utf-8')

        f.seek(0x28, 0)
        self.DexHeader.endian_tag = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode('utf-8')

        f.seek(0x2c, 0)
        self.DexHeader.link_size = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode('utf-8')

        f.seek(0x30, 0)
        self.DexHeader.link_off = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode('utf-8')

        f.seek(0x34, 0)
        self.DexHeader.map_off = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode('utf-8')

        f.seek(0x38, 0)
        self.DexHeader.string_ids_size = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode('utf-8')

        f.seek(0x3c, 0)
        self.DexHeader.string_ids_off = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode('utf-8')

        f.seek(0x40, 0)
        self.DexHeader.type_ids_size = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode('utf-8')

        f.seek(0x44, 0)
        self.DexHeader.type_ids_off = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode('utf-8')

        f.seek(0x48, 0)
        self.DexHeader.proto_ids_size = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode('utf-8')
        
        f.seek(0x4c, 0)
        self.DexHeader.proto_ids_off = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode('utf-8')

        f.seek(0x50, 0)
        self.DexHeader.field_ids_size = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode()

        f.seek(0x54, 0)
        self.DexHeader.field_ids_off = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode()

        f.seek(0x58, 0)
        self.DexHeader.methodIdsSize = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode()

        f.seek(0x5c, 0)
        self.DexHeader.methodIdsOff = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode()

        f.seek(0x60, 0)
        self.DexHeader.classDefsSize = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode()

        f.seek(0x64, 0)
        self.DexHeader.classDefsOff = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode()

        f.seek(0x68, 0)
        self.DexHeader.dataSize = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode()

        f.seek(0x6c, 0)
        self.DexHeader.dataOff = bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode()

    def print_header(self):
        print("[+] magic : {magic}".format(magic = self.DexHeader.magic))
        print("[+] checksum : {checksum}".format(checksum = self.DexHeader.checksum))
        print("[+] signature : {signature}".format(signature = self.DexHeader.signature))
        print("[+] file_size : {file_size}".format(file_size = self.DexHeader.file_size))
        print("[+] header_size : {header_size}".format(header_size = self.DexHeader.header_size))
        print("[+] endian_tag : {endian_tag}".format(endian_tag = self.DexHeader.endian_tag))
        print("[+] link_size : {link_size}".format(link_size = self.DexHeader.link_size))
        print("[+] link_off : {link_off}".format(link_off = self.DexHeader.link_off))
        print("[+] map_off : {map_off}".format(map_off = self.DexHeader.map_off))
        print("[+] string_ids_size : {string_ids_size}".format(string_ids_size = self.DexHeader.string_ids_size))
        print("[+] string_ids_off : {string_ids_off}".format(string_ids_off = self.DexHeader.string_ids_off))
        print("[+] type_ids_size : {type_ids_size}".format(type_ids_size = self.DexHeader.type_ids_size))
        print("[+] type_ids_off : {type_ids_off}".format(type_ids_off = self.DexHeader.type_ids_off))
        print("[+] proto_ids_size : {proto_ids_size}".format(proto_ids_size = self.DexHeader.proto_ids_size))
        print("[+] proto_ids_off : {proto_ids_off}".format(proto_ids_off = self.DexHeader.proto_ids_off))
        print("[+] field_ids_size : {field_ids_size}".format(field_ids_size = self.DexHeader.field_ids_size))
        print("[+] field_ids_off : {field_ids_off}".format(field_ids_off = self.DexHeader.field_ids_off))
        print("[+] methodIdsSize : {methodIdsSize}".format(methodIdsSize = self.DexHeader.methodIdsSize))
        print("[+] methodIdsOff : {methodIdsOff}".format(methodIdsOff = self.DexHeader.methodIdsOff))
        print("[+] classDefsSize : {classDefsSize}".format(classDefsSize = self.DexHeader.classDefsSize))
        print("[+] classDefsOff : {classDefsOff}".format(classDefsOff = self.DexHeader.classDefsOff))
        print("[+] dataSize : {dataSize}".format(dataSize = self.DexHeader.dataSize))
        print("[+] dataOff : {dataOff}".format(dataOff = self.DexHeader.dataOff))

    def init_stringids(self):
        string_ids_off = int(self.DexHeader.string_ids_off, 16)
        string_ids_size =  int(self.DexHeader.string_ids_size, 16)

        for i in range(string_ids_size):
            self.DexHeader.f.seek(string_ids_off + i * 4, 0)
            string_data_off = int(bytes.fromhex(binascii.b2a_hex(self.DexHeader.f.read(1)[::-1]).hex()).decode(), 16)
            self.DexHeader.f.seek(string_data_off, 0)

            #pass the length byte
            self.DexHeader.f.read(1)

            length = 0
            while int(bytes.fromhex(binascii.b2a_hex(self.DexHeader.f.read(1)[::-1]).hex()).decode(), 16) != 0:
                length += 1 

            self.DexHeader.f.seek(string_data_off + 1, 0)
            string_data = self.DexHeader.f.read(length)
            self.DexStringIds.append(string_data)

            string_ids_off += 2 #pass \0 and length byte

    def print_stringids(self):
        print("\n")
        print("[+]DexStringList")
        for i in range(len(self.DexStringIds)):
            print("{index} : {string}".format(index = hex(i), string = self.DexStringIds[i]))

def main():
    dex = Dexfile("classes.dex")
    dex.print_header()


if __name__ == '__main__':
    main()






