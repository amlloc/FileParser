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
        self.dexHeader = DexHeader()
        self.DexStringIds        = []
        self.DexTypeIds          = []
        self.DexFieldIds         = []
        self.DexMethodIds        = []
        self.DexProtoIds         = []
        self.DexClassDefs        = []
        self.dexMapList          = None

        self.init_header()

        # self.init_map_list()

        self.init_stringids()
        # self.print_stringids()
        self.init_typeids()
        # self.print_types()
        self.init_field_ids()
        # self.print_fieldids()

        self.init_proto_ids()
        # self.print_proto_ids()

        self.init_method_ids()
        # self.print_method_ids()
        
        self.init_class_defs()
        self.print_class_defs()
        





    def init_header(self):

        f = open(self.filePath, "rb")
        self.dexHeader.f = f
        f.seek(0x0, 0)
        self.dexHeader.magic = binascii.b2a_hex(f.read(8))
        f.seek(0x8, 0)
        #binary data -> reverse data -> Hexadecimal data -> Hexadecimal string  -> Hexadecimal
        self.dexHeader.checksum = binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8')
        f.seek(0xc, 0)
        self.dexHeader.signature = binascii.b2a_hex(f.read(20))

        f.seek(0x20, 0)
        # a = f.read(4)[::-1] # b'\x00u!\x90'
        # b = binascii.b2a_hex(a)  # b'00752190'
        # c = b.hex() #多余        '3030373532313930'
        # d = bytes.fromhex(c)  #多余  b'00752190'
        # e = d.decode('utf-8')  #'00752190'
        # self.dexHeader.file_size = int(bytes.fromhex(binascii.b2a_hex(f.read(4)[::-1]).hex()).decode('utf-8'),16)
        self.dexHeader.file_size = int(binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8'),16)

        f.seek(0x24, 0)
        self.dexHeader.header_size = int(binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8'),16)

        f.seek(0x28, 0)
        self.dexHeader.endian_tag = binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8')

        f.seek(0x2c, 0)
        self.dexHeader.link_size = int(binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8'),16)

        f.seek(0x30, 0)
        self.dexHeader.link_off = int(binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8'),16)

        f.seek(0x34, 0)
        self.dexHeader.map_off =int(binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8'),16)

        f.seek(0x38, 0)
        self.dexHeader.string_ids_size = int(binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8'),16)

        f.seek(0x3c, 0)
        self.dexHeader.string_ids_off = int(binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8'),16)

        f.seek(0x40, 0)
        self.dexHeader.type_ids_size = int(binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8'),16)

        f.seek(0x44, 0)
        self.dexHeader.type_ids_off = int(binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8'),16)

        f.seek(0x48, 0)
        self.dexHeader.proto_ids_size = int(binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8'),16)
        
        f.seek(0x4c, 0)
        self.dexHeader.proto_ids_off = int(binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8'),16)

        f.seek(0x50, 0)
        self.dexHeader.field_ids_size = int(binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8'),16)

        f.seek(0x54, 0)
        self.dexHeader.field_ids_off = int(binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8'),16)

        f.seek(0x58, 0)
        self.dexHeader.method_ids_size = int(binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8'),16)

        f.seek(0x5c, 0)
        self.dexHeader.method_ids_off = int(binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8'),16)

        f.seek(0x60, 0)
        self.dexHeader.class_defs_size = int(binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8'),16)

        f.seek(0x64, 0)
        self.dexHeader.class_defs_off = int(binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8'),16)

        f.seek(0x68, 0)
        self.dexHeader.data_size = int(binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8'),16)

        f.seek(0x6c, 0)
        self.dexHeader.data_off = int(binascii.b2a_hex(f.read(4)[::-1]).decode('utf-8'),16)



    def init_map_list(self):
        map_off = int(self.dexHeader.map_off, 16)
        self.dexHeader.f.seek(map_off, 0)
        map_size = int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'), 16)
        map_list = []
        for i in range(map_size):
            self.dexHeader.f.seek(map_off + i * 12 + 4, 0)
            map_item_type = int(binascii.b2a_hex(self.dexHeader.f.read(2)[::-1]).decode('utf-8'), 16)
            map_item_unused = int(binascii.b2a_hex(self.dexHeader.f.read(2)[::-1]).decode('utf-8'), 16)
            map_item_size = int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'), 16)
            map_item_offset = int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'), 16)

            map_list.append(DexMapItem(map_item_type, map_item_unused, map_item_size, map_item_offset))
        
        self.dexMapList = DexMapList(map_size, map_list)

    def init_stringids(self):
        string_ids_off = self.dexHeader.string_ids_off
        string_ids_size =  self.dexHeader.string_ids_size

        for i in range(string_ids_size):
            self.dexHeader.f.seek(string_ids_off + i * 4, 0)
            string_data_off = int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'), 16)
            self.dexHeader.f.seek(string_data_off, 0)

            #pass the length byte
            self.dexHeader.f.read(1)

            length = 0

            str = binascii.b2a_hex(self.dexHeader.f.read(1)[::-1]).decode('utf-8')
            while str != '' and  int(str, 16) != 0:
                str = binascii.b2a_hex(self.dexHeader.f.read(1)[::-1]).decode('utf-8')
                length += 1 

            self.dexHeader.f.seek(string_data_off + 1, 0)
            string_data = self.dexHeader.f.read(length)

            self.dexHeader.f.read(1) # remove \x00
            string_data_off += (length + 2) # + \0 + size bit

            # self.DexStringIds.append(string_data.decode())
            self.DexStringIds.append(string_data)



    def init_typeids(self):
        type_ids_off = self.dexHeader.type_ids_off
        type_ids_size = self.dexHeader.type_ids_size

        for i in range(type_ids_size):
            self.dexHeader.f.seek(type_ids_off + i * 4, 0)
            descriptor_idx = int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'), 16)
            dex_type_id = DexTypeId(descriptor_idx)
            self.DexTypeIds.append(dex_type_id)



    def init_field_ids(self):
        field_off = self.dexHeader.field_ids_off
        field_size = self.dexHeader.field_ids_size

        for i in range(field_size):
            self.dexHeader.f.seek(field_off + i * 8, 0)
            # u2 class_idx
            class_idx = int(binascii.b2a_hex(self.dexHeader.f.read(2)[::-1]).decode('utf-8'), 16)
            # u2 type_idx
            type_idx = int(binascii.b2a_hex(self.dexHeader.f.read(2)[::-1]).decode('utf-8'), 16)
            # u4 name_idx
            name_idx = int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'), 16)

            field_id = DexFieldId(class_idx, type_idx, name_idx)
            field_id.offset = field_off + i * 8
            field_id.length = 8
            self.DexFieldIds.append(field_id)




    def init_method_ids(self):
        method_off = self.dexHeader.method_ids_off
        method_size = self.dexHeader.method_ids_size

        for i in range(method_size):
            self.dexHeader.f.seek(method_off + i * 8, 0)
            class_idx = int(binascii.b2a_hex(self.dexHeader.f.read(2)[::-1]).decode('utf-8'), 16)
            proto_idx = int(binascii.b2a_hex(self.dexHeader.f.read(2)[::-1]).decode('utf-8'), 16)
            name_idx = int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'), 16)

            method_id = DexMethodId(class_idx, proto_idx, name_idx)
            method_id.offset = method_off + i * 8
            method_id.length = 8
            self.DexMethodIds.append(method_id)
    

        

    def init_proto_ids(self):
        proto_ids_off = self.dexHeader.proto_ids_off
        proto_ids_size = self.dexHeader.proto_ids_size

        for i in range(proto_ids_size):
            self.dexHeader.f.seek(proto_ids_off + i * 12, 0)
            shorty_idx =  int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'), 16)
            return_type_idx = int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'), 16)
            parameters_off = int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'), 16)

            proto_id_item = DexProtoId(shorty_idx, return_type_idx, parameters_off)
            proto_id_item.offset = proto_ids_off + proto_ids_size
            proto_id_item.length = 12

            if parameters_off == 0:
                proto_id_item.dexTypeList = None
                self.DexProtoIds.append(proto_id_item)
                continue
            self.dexHeader.f.seek(parameters_off, 0)

            parameter_str = ""
            # Struct DexTypeList
            # u4 size
            dex_type_item_size  = int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'), 16)

            # DexTypeItem list[]
            dexTypeListObj = DexTypeList()
            dexTypeListObj.size = dex_type_item_size
            for i in range(dex_type_item_size):
                # Struct DexTypeItem
                # u2 typeIdx
                typeIdx = int(binascii.b2a_hex(self.dexHeader.f.read(2)[::-1]).decode('utf-8'), 16)
                dexTypeListObj.list.append(typeIdx)

            proto_id_item.dexTypeList = dexTypeListObj
            self.DexProtoIds.append(proto_id_item)

    def readUnsignedLeb128(self, hex_value):
        byte_count = len(hex_value) / 2
        byte_count_int = int(byte_count)

        index = 0
        for i in range(byte_count_int):
            v1 = int(hex_value[i * 2 : i * 2 + 2], 16)
            if v1 > 0:
                index = index
                break
        
        result = 0
        hex_value = hex_value[index * 2:]
        byte_count = len(hex_value) / 2
        byte_count_int = int(byte_count)
        for i in range(byte_count_int):
            cur = int(hex_value[i * 2:i * 2 + 2], 16)
            if cur > 0x7f:
                result = result | ((cur & 0x7f) <<(7 * i))
            else:
                result = result | ((cur & 0x7f) << (7 * i))
                break
        
        return result

    def init_class_defs(self):
        class_defs_off = self.dexHeader.class_defs_off
        class_defs_size = self.dexHeader.class_defs_size
        
        

        for i in range(class_defs_size):
            
            self.dexHeader.f.seek(class_defs_off + i * 32, 0)
            class_idx = int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'), 16)
            access_flags = int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'), 16)
            superclass_idx = int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'), 16)
            interfaces_off = int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'), 16)
            source_file_idx = int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'), 16)
            annotations_off = int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'), 16)
            class_data_off = int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'), 16)
            static_values_off = int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'), 16)


            dexClassDefObj = DexClassDef(class_idx, access_flags, superclass_idx, interfaces_off, source_file_idx, annotations_off, class_data_off,  static_values_off)
            dexClassDefObj.offset = class_defs_off + i * 32
            dexClassDefObj.length = 32

            self.DexClassDefs.append(dexClassDefObj)
            if class_data_off == 0:
                continue

            # 获取DexClassData结构
            ##########################
            dexClassData = DexClassData() 

            #解析DexClassData结构体中的header成员
            dexClassDataHeader = class_data_off
            dexClassDataHeaderLength = 0

            self.dexHeader.f.seek(class_data_off, 0)
     
            dexClassDataHeader = []
            for i in range(4):
                cur_bytes_hex = binascii.b2a_hex(self.dexHeader.f.read(1)) 
                dexClassDataHeaderLength +=1 #每读一个字节，长度+1
                cur_bytes = int(cur_bytes_hex, 16)
                value = cur_bytes_hex

                while cur_bytes > 0x7f:
                    cur_bytes_hex = binascii.b2a_hex(self.dexHeader.f.read(1)) 
                    dexClassDataHeaderLength +=1    #每读一个字节，长度+1
                    cur_bytes = int(cur_bytes_hex, 16)
                    value += cur_bytes_hex
                    
                dexClassDataHeader.append(value)
            
            static_fields_size = self.readUnsignedLeb128(dexClassDataHeader[0])
            instance_fields_size = self.readUnsignedLeb128(dexClassDataHeader[1])
            direct_method_size  =  self.readUnsignedLeb128(dexClassDataHeader[2])
            virtual_method_size = self.readUnsignedLeb128(dexClassDataHeader[3])
 
            dexClassDataHeader = DexClassDataHeader(static_fields_size, instance_fields_size, direct_method_size, virtual_method_size)
            dexClassDataHeader.length = dexClassDataHeaderLength
            dexClassDataHeader.offset = class_data_off
            
            dexClassData.header = dexClassDataHeader


            

            # 解析DexClassData结构体的staticFields、instanceFields、directMethods 和 virtualMethods
            offset = dexClassDataHeader.offset + dexClassDataHeader.length
            # 解析DexField* staticFields 成员
            """
            struct DexField{
                u4 fieldIdx;
                u4 accessFlags;
            }
            """

            for i in range(static_fields_size):
                array = []
                length = 0
                for j in range(2):
                    cur_bytes_hex = binascii.b2a_hex(self.dexHeader.f.read(1))
                    length +=1
                    value = cur_bytes_hex
                    cur_bytes = int(cur_bytes_hex, 16)

                    while cur_bytes > 0x7f:
                        cur_bytes_hex = binascii.b2a_hex(self.dexHeader.f.read(1))
                        length += 1
                        
                        cur_bytes = int(cur_bytes_hex, 16)
                        value += cur_bytes_hex
                        
                    array.append(value)

                field_idx = self.readUnsignedLeb128(array[0])
                access_flags = self.readUnsignedLeb128(array[1])

                staticDexField = DexField(field_idx, access_flags)
                staticDexField.offset = offset
                staticDexField.length = length

                dexClassData.static_fields.append(staticDexField)
                offset += length            

            # (2)解析DexField* instanceFields成员
            for i in range(instance_fields_size):
                array = []
                length = 0
                for j in range(2):
                    cur_bytes_hex = binascii.b2a_hex(self.dexHeader.f.read(1))
                    length += 1
                    
                    cur_bytes = int(cur_bytes_hex, 16)
                    value += cur_bytes_hex
                
                    # 字节大于0x7f时说明有下一位
                    while cur_bytes > 0x7f:
                        cur_bytes_hex = binascii.b2a_hex(self.dexHeader.f.read(1))
                        length += 1
                        cur_bytes = int(cur_bytes_hex, 16)
                        #构造UnsignedLeb128格式表示的二进制数据
                        value += cur_bytes_hex
                
                    array.append(value)

                field_idx =self.readUnsignedLeb128(array[0])
                access_flags = self.readUnsignedLeb128(array[1])

                dexField = DexField(field_idx, access_flags)
                dexField.offset = offset
                dexField.length = length

                dexClassData.instance_fields.append(dexField)

            # (3)解析DexMethod* directMethods成员
            for i in range(direct_method_size):
                array = []
                length = 0
                for j in range(3):
                    cur_bytes_hex = binascii.b2a_hex(self.dexHeader.f.read(1))
                    length += 1
                    
                    cur_bytes = int(cur_bytes_hex, 16)
                    value += cur_bytes_hex
                
                    while cur_bytes > 0x7f:
                        cur_bytes_hex = binascii.b2a_hex(self.dexHeader.f.read(1))
                        length += 1
                        cur_bytes = int(cur_bytes_hex, 16)
                        value += cur_bytes_hex
                
                    array.append(value)

                method_idx = self.readUnsignedLeb128(array[0])
                access_flags = self.readUnsignedLeb128(array[1])
                code_off = self.readUnsignedLeb128(array[2])

                dexMethod = DexMethod(method_idx, access_flags, code_off)
                dexMethod.offset = offset
                dexMethod.length = length

                dexClassData.direct_methods.append(dexMethod)
                offset += length

            # (4)解析DexMethod* virtualMethods成员
            for i in range(virtual_method_size):
                array = []
                length = 0
                for j in range(3):
                    cur_bytes_hex = binascii.b2a_hex(self.dexHeader.f.read(1))
                    length += 1
                    
                    cur_bytes = int(cur_bytes_hex, 16)
                    value += cur_bytes_hex
                
                    while cur_bytes > 0x7f:
                        cur_bytes_hex = binascii.b2a_hex(self.dexHeader.f.read(1))
                        length += 1
                        cur_bytes = int(cur_bytes_hex, 16)
                        value += cur_bytes_hex
                
                    array.append(value)

                method_idx = self.readUnsignedLeb128(array[0])
                access_flags = self.readUnsignedLeb128(array[1])
                code_off = self.readUnsignedLeb128(array[2])

                dexMethod = DexMethod(method_idx, access_flags, code_off)
                dexMethod.offset = offset
                dexMethod.length = length

                dexClassData.virtual_methods.append(dexMethod)
                offset += length
        
        dexClassDefObj.dexClassData = dexClassData
        
        for dexMethod in dexClassDefObj.dexClassData.direct_methods:
            if dexMethod.code_off != 0:
                dexCode = self.parseDexCode(dexMethod.code_off)
                dexMethod.dex_code = dexCode
            else:
                dexMethod.dex_code = None
        
        for dexMethod in dexClassDefObj.dexClassData.virtual_methods:
            if dexMethod.code_off != 0:
                dexCode = self.parseDexCode(dexMethod.code_off)
                dexMethod.dex_code = dexCode
            else:
                dexMethod.dex_code = None

    def print_header(self):
        print("[+] magic : {magic}".format(magic = self.dexHeader.magic))
        print("[+] checksum : {checksum}".format(checksum = self.dexHeader.checksum))
        print("[+] signature : {signature}".format(signature = self.dexHeader.signature))
        print("[+] file_size : {file_size}".format(file_size = self.dexHeader.file_size))
        print("[+] header_size : {header_size}".format(header_size = self.dexHeader.header_size))
        print("[+] endian_tag : {endian_tag}".format(endian_tag = self.dexHeader.endian_tag))
        print("[+] link_size : {link_size}".format(link_size = self.dexHeader.link_size))
        print("[+] link_off : {link_off}".format(link_off = self.dexHeader.link_off))
        print("[+] map_off : {map_off}".format(map_off = self.dexHeader.map_off))
        print("[+] string_ids_size : {string_ids_size}".format(string_ids_size = self.dexHeader.string_ids_size))
        print("[+] string_ids_off : {string_ids_off}".format(string_ids_off = self.dexHeader.string_ids_off))
        print("[+] type_ids_size : {type_ids_size}".format(type_ids_size = self.dexHeader.type_ids_size))
        print("[+] type_ids_off : {type_ids_off}".format(type_ids_off = self.dexHeader.type_ids_off))
        print("[+] proto_ids_size : {proto_ids_size}".format(proto_ids_size = self.dexHeader.proto_ids_size))
        print("[+] proto_ids_off : {proto_ids_off}".format(proto_ids_off = self.dexHeader.proto_ids_off))
        print("[+] field_ids_size : {field_ids_size}".format(field_ids_size = self.dexHeader.field_ids_size))
        print("[+] field_ids_off : {field_ids_off}".format(field_ids_off = self.dexHeader.field_ids_off))
        print("[+] methodIdsSize : {methodIdsSize}".format(methodIdsSize = self.dexHeader.method_ids_size))
        print("[+] methodIdsOff : {methodIdsOff}".format(methodIdsOff = self.dexHeader.method_ids_off))
        print("[+] classDefsSize : {classDefsSize}".format(classDefsSize = self.dexHeader.class_defs_size))
        print("[+] classDefsOff : {classDefsOff}".format(classDefsOff = self.dexHeader.class_defs_off))
        print("[+] dataSize : {dataSize}".format(dataSize = self.dexHeader.data_size))
        print("[+] dataOff : {dataOff}".format(dataOff = self.dexHeader.data_off))

    #todo
    def print_class_defs(self):
        print()
    
    def print_proto_ids(self):
        print("\n")
        print("[+]DexProtoIds")
        proto_ids_off = self.dexHeader.proto_ids_off
        self.dexHeader.f.seek(proto_ids_off, 0)

        for index in range(len(self.DexProtoIds)):

            proto_id_item = self.DexProtoIds[index]
            shorty_idx = proto_id_item.shorty_idx
            return_type_idx = proto_id_item.return_type_idx
            parameters_off = proto_id_item.parameters_off

            shorty_str = self.getStringId(shorty_idx)
            return_type_str = self.getDexTypeId(return_type_idx)
            # Struct DexProtoId
            # u4 shortyIdx
            # u4 returnTypeIdx
            # u4 parametersOff
            print("#{index} ({start} ~ {end})".format(index = str(index), start = hex(proto_id_item.offset), end = hex(proto_id_item.offset + index * 12)))
            print("DexProtoId[{index}] -> shorty_idx= {shorty_idx}\t#{shorty_str}".format(index = str(index), shorty_idx = hex(shorty_idx), shorty_str = shorty_str))
            print("DexProtoId[{index}] -> return_type_idx= {return_type_idx}\t#{return_type_str}".format(index = str(index), return_type_idx = hex(return_type_idx), return_type_str = return_type_str))
            print("DexProtoId[{index}] -> parameters_off= {parameters_off}".format(index = str(index), parameters_off = hex(parameters_off)))

            if proto_id_item.dexTypeList:
                print("DexTypeList size - > {0}".format(str(proto_id_item.dexTypeList.size)))
                for j in range(proto_id_item.dexTypeList.size):
                    print("DexTypeList->list[{}]={}\t#{}".format(str(j), proto_id_item.dexTypeList.list[j], self.getDexTypeId(proto_id_item.dexTypeList.list[j])))
            
            print('')

    def print_fieldids(self):
        print("\n")
        print("[+]DexFieldIds")
        for i in range(len(self.DexFieldIds)):
            field_offset = self.DexFieldIds[i].offset

            # DexFieldId
            # u2 class_idx
            class_idx = self.DexFieldIds[i].class_idx
            # u2 type_idx
            type_idx = self.DexFieldIds[i].type_idx
            # u4 name_idx
            name_idx = self.DexFieldIds[i].name_idx

            print("#{index} : {start} ~ {end}".format(index = hex(i), start = hex(field_offset), end = hex(field_offset + self.DexFieldIds[i].length)))

            print("DexFieldIds[{index}] -> class_idx = {class_idx}\t# {class_idx_str}".format(index = hex(i), class_idx = hex(class_idx), class_idx_str = self.getStringId(class_idx)))
            print("DexFieldIds[{index}] -> type_idx = {type_idx}\t# {type_idx_str}".format(index = hex(i), type_idx = hex(type_idx), type_idx_str = self.getStringId(type_idx)))
            print("DexFieldIds[{index}] -> name_idx = {name_idx}\t# {name_idx_str}".format(index = hex(i), name_idx = hex(class_idx), name_idx_str = self.getStringId(name_idx)))
            
    def print_stringids(self):
        print("\n")
        print("[+]DexStringList")
        for i in range(len(self.DexStringIds)):
            print("#{index} : {string}".format(index = hex(i), string = self.DexStringIds[i]))

    def print_types(self):
        print("\n")
        print("[+]DexTypeList")
        for i in range(len(self.DexTypeIds)):
            print("#{index} : {string}".format(index = hex(i), string = self.getTypeId(i)))
        print("\n")

    def print_method_ids(self):
        print("\n")
        print("[+]DexMethodIds")
        for i in range(len(self.DexFieldIds)):
            field_offset = self.DexFieldIds[i].offset

            # DexFieldId
            # u2 class_idx
            class_idx = self.DexMethodIds[i].class_idx
            # u2 type_idx
            proto_idx = self.DexMethodIds[i].proto_idx
            # u4 name_idx
            name_idx = self.DexMethodIds[i].name_idx

            print("#{index} : {start} ~ {end}".format(index = hex(i), start = hex(field_offset), end = hex(field_offset + self.DexFieldIds[i].length)))

            print("DexMethodIds[{index}] -> class_idx = {class_idx}\t# {class_idx_str}".format(index = str(i), class_idx = hex(class_idx), class_idx_str = self.getStringId(class_idx)))
            print("DexMethodIds[{index}] -> proto_idx = {proto_idx}\t# {proto_idx_str}".format(index = str(i), proto_idx = hex(proto_idx), proto_idx_str = self.DexProtoIds[proto_idx].toString(self)))
            print("DexMethodIds[{index}] -> name_idx = {name_idx}\t# {name_idx_str}".format(index = str(i), name_idx = hex(class_idx), name_idx_str = self.getStringId(name_idx)))

    def getTypeId(self, index):
        return self.DexStringIds[self.DexTypeIds[index].descriptor_idx]

    def getStringId(self, shortyIdx):
        return self.DexStringIds[shortyIdx]
    
    def getDexTypeId(self, returnTypeIdx):
        return self.DexStringIds[self.DexTypeIds[returnTypeIdx].descriptor_idx]
            
    def parseDexCode(self, code_off):
        self.dexHeader.f.seek(code_off, 0)
        registers_size = int(binascii.b2a_hex(self.dexHeader.f.read(2)[::-1]).decode('utf-8'),16)
        ins_size = int(binascii.b2a_hex(self.dexHeader.f.read(2)[::-1]).decode('utf-8'),16)
        outs_size = int(binascii.b2a_hex(self.dexHeader.f.read(2)[::-1]).decode('utf-8'),16)
        tries_size = int(binascii.b2a_hex(self.dexHeader.f.read(2)[::-1]).decode('utf-8'),16)
        debug_info_off = int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'),16)
        insns_size = int(binascii.b2a_hex(self.dexHeader.f.read(4)[::-1]).decode('utf-8'),16)
        insns = ''

        #todo insns define
        if insns_size == 0:
            insns = ''
        else:
            insns = ''
            if insns_size * 2 > sys.maxsize:
                size = insns_size * 2
                while size > sys.maxsize:
                    insns += binascii.b2a_hex(self.dexHeader.f.read(sys.maxsize)).decode('utf-8')
                    size -= sys.maxsize
                # 末尾insns数据
                if size > 0:
                    insns += binascii.b2a_hex(self.dexHeader.f.read(size)).decode('utf-8')
            else:
                insns +=  binascii.b2a_hex(self.dexHeader.f.read(insns_size)).decode('utf-8')

        dex_code = DexCode()
        dex_code.registers_size = registers_size
        dex_code.ins_size = ins_size
        dex_code.outs_size = outs_size
        dex_code.tries_size = tries_size
        dex_code.debug_info_off = debug_info_off
        dex_code.insns_size = insns_size
        dex_code.insns = insns
        dex_code.offset = code_off
        dex_code.length = 16 * len(insns) / 2 

        return dex_code

    # def dumpDexCode(self, dexMethod):
    #     if dexMethod.dex_code == None:
    #         return
    #     print("# {} ~ {} ".format(hex(dexMethod.dex_code.offset), hex(dexMethod.dex_code.)))
    
            
def main():
    dex = Dexfile("classes.dex")
    dex.print_header()


if __name__ == '__main__':
    main()