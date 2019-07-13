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

class DexMap:
    def __init__(self):
        self.type            = None
        self.unused          = None
        self.size            = None
        self.offset          = None

class DexStringData:
    def __init__(self):
        self.utf16_size      = None
        self.data            = None

class DexTypeId:
    def __init__(self):
        self.descriptor_idx  = None

class DexProtoId:
    def __init__(self):
        self.shorty_idx      = None
        self.return_type_idx = None
        self.parameters_off  = None

class DexFieldId:
    def __init__(self):
        self.class_idx       = None
        self.type_idx        = None
        self.name_idx        = None

class DexMethodId:
    def __init__(self):
        self.class_idx       = None
        self.proto_idx       = None
        self.name_idx        = None

class DexClassDef:
    def __init__(self):
        self.class_idx           = None
        self.access_flags        = None
        self.superclass_idx      = None
        self.interfaces_off      = None
        self.source_file_idx     = None
        self.annotations_off     = None
        self.class_data_off      = None
        self.static_values_off   = None

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
    def __init__(self):
        self.static_fields_size   = None
        self.instance_fields_size = None
        self.direct_method_size   = None
        self.virtual_method_size  = None
        self.static_field         = None
        self.instance_fields      = None
        self.direct_methods       = None
        self.virtual_methods      = None

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