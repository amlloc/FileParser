class DexHeader:
    # struct DexHeader {
    #     u1  magic[8];           /* includes version number */
    #     u4  checksum;           /* adler32 checksum */
    #     u1  signature[kSHA1DigestLen]; /* SHA-1 hash */
    #     u4  fileSize;           /* length of entire file */
    #     u4  headerSize;         /* offset to start of next section */
    #     u4  endianTag;
    #     u4  linkSize;
    #     u4  linkOff;
    #     u4  mapOff;
    #     u4  stringIdsSize;
    #     u4  stringIdsOff;
    #     u4  typeIdsSize;
    #     u4  typeIdsOff;
    #     u4  protoIdsSize;
    #     u4  protoIdsOff;
    #     u4  fieldIdsSize;
    #     u4  fieldIdsOff;
    #     u4  methodIdsSize;
    #     u4  methodIdsOff;
    #     u4  classDefsSize;
    #     u4  classDefsOff;
    #     u4  dataSize;
    #     u4  dataOff;
    # };
    def __init__(self):
        self.f               = None
        self.magic           = None
        self.checksum        = None
        self.signature       = None
        self.file_size       = None
        self.header_size     = None
        self.endian_tag      = None
        self.link_size       = None
        self.link_off        = None
        self.map_off         = None
        self.string_ids_size = None
        self.string_ids_off  = None
        self.type_ids_size   = None
        self.type_ids_off    = None
        self.proto_ids_size  = None
        self.proto_ids_off   = None
        self.field_ids_size  = None
        self.field_ids_off   = None
        self.method_ids_size = None
        self.method_ids_off  = None
        self.class_defs_size = None
        self.class_defs_off  = None
        self.data_size       = None
        self.data_off        = None

class DexMapItem:
    def __init__(self, type, unused, size, offset):
        self.type            = type
        self.unused          = unused
        self.size            = size
        self.offset          = offset

class DexMapList:
    def __init__(self, size, list):
        self.size            = None
        self.list            = list

class DexStringData:
    def __init__(self):
        self.utf16_size      = None
        self.data            = None

class DexTypeId:
    def __init__(self, descriptor_idx):
        self.descriptor_idx  = descriptor_idx

class DexProtoId:
    def __init__(self, shorty_idx, return_type_idx, parameters_off):
        self.shorty_idx      = shorty_idx
        self.return_type_idx = return_type_idx
        self.parameters_off  = parameters_off

class DexFieldId:
    def __init__(self, class_idx, type_idx, name_idx):
        self.class_idx       = class_idx
        self.type_idx        = type_idx
        self.name_idx        = name_idx

class DexMethodId:
    def __init__(self, class_idx, proto_idx, name_idx):
        self.class_idx       = class_idx
        self.proto_idx       = proto_idx
        self.name_idx        = name_idx

class DexClassDef:
    def __init__(self, class_idx, access_flags, superclass_idx, interfaces_off, source_file_idx, annotations_off, class_data_off, static_values_off):
        self.class_idx           = class_idx
        self.access_flags        = access_flags
        self.superclass_idx      = interfaces_off
        self.interfaces_off      = interfaces_off
        self.source_file_idx     = source_file_idx
        self.annotations_off     = annotations_off
        self.class_data_off      = class_data_off
        self.static_values_off   = static_values_off

class DexCallSiteId:
    def __init__(self):
        self.call_site_off       = None

class DexMethodHandle:
    def __init__(self):
        self.method_handle_type  = None
        self.unused              = None
        self.field_or_method_id  = None
        self.unused

class DexClassData:
    def __init__(self, header, static_field, instance_fields, direct_methods, virtual_methods):
        self.header               = header
        self.static_field         = static_field
        self.instance_fields      = instance_fields
        self.direct_methods       = direct_methods
        self.virtual_methods      = virtual_methods

class DexClassDataHeader:
    def __init__(self, static_fields_size, instance_fields_size, direct_method_size, virtual_method_size):
        self.static_fields_size   = static_fields_size
        self.instance_fields_size = instance_fields_size
        self.direct_method_size   = direct_method_size
        self.virtual_method_size  = virtual_method_size

class DexField:
    def __init__(self, field_idx, access_flags):
        self.field_idx            = field_idx
        self.access_flags         = access_flags

class DexMethod:
    def __init__(self, method_idx, access_flags, code_off):
        self.method_idx           = method_idx
        self.access_flags         = access_flags
        self.code_off             = code_off

class DexCode:
    def __init__(self, registers_size, ins_size, outs_size, tries_size, debug_info_off, insns_size, insns):
        self.registers_size      = registers_size
        self.ins_size            = ins_size
        self.outs_size           = outs_size
        self.tries_size          = tries_size
        self.debug_info_off      = debug_info_off
        self.insns_size          = insns_size
        self.insns               = insns


class DexEncodedField:
    def __init__(self):
        self.field_idx_diff       = None
        self.access_flags         = None

class DexEndcodedMethod:
    def __init__(self):
        self.method_idx_diff      = None
        self.access_flags         = None
        self.code_off             = None

class DexTypeList:
    def __init__(self):
        self.size                 = None
        self.list                 = []            

class DexTypeItem:
    def __init__(self):
        self.type_idx             = None

class DexCodeItem:
    def __init__(self):
        self.registers_size     = None
        self.ins_size           = None
        self.outs_size          = None
        self.tries_size         = None
        self.debug_info_off     = None
        self.insns_size         = None
        self.insns              = None
        self.padding            = None
        self.tries_size         = None
        self.handlers           = None

class DexTryItem:
    def __init__(self):
        self.start_addr         = None
        self.insn_count         = None
        self.handler_off        = None

class DexEncodedCatchHandlerList:
    def __init__(self):
        self.size               = None
        self.list               = []

class DexEncodedCatchHandler:
    def __init__(self):
        self.size               = None
        self.handlers           = []
        self.catch_all_addr     = None
    
class DexEncodedTypeAddrPair:
    def __init__(self):
        self.type               = None
        self.addr               = None

        
class DexDebugInfoItem:
    def __init__(self):
        self.line_start         = None
        self.parameters_size    = None
        self.parameter_names    = []

class DexAnnotationDirectoryItem:
    def __init__(self):
        self.class_annotations_off      = None
        self.fields_size                = None
        self.annotated_methods_size     = None
        self.annotated_parameters_size  = None

class DexFieldAnnotation:
    def __init__(self):
        self.field_idx                  = None
        self.annotations_off            = None

class DexMethodAnnotation:
    def __init__(self): 
        self.method_idx                 = None
        self.annotations_off            = None

class DexParameterAnnotation:
    def __init__(self):
        self.method_idx                 = None
        self.annotations_off            = None

class DexAnnotationSetRefList:
    def __init__(self):
        self.size  = None 
        self.list  = []

class DexAnnotationSetRefItem:
    def __init__(self):
        self.annotation_off         = None

class DexAnnotationSetItem:
    def __init__(self):
        self.size                   = None
        self.entries                = []

class DexAnmnotationOffItem:
    def __init__(self):
        self.annotation_off         = None

class DexAnnotationItem:
    def __init__(self):
        self.visibility             = None
        self.annotation             = None


class DexEncodedArrayItem:
    def __init__(self):
        self.value                  = None