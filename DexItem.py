class DexHeader:
    def __init__(self):
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
        self.class_idx       = None
        self.access_flags    = None
        self.superclass_idx  = None
        self.interfaces_off  = None
        self.source_file_idx = None
        self.annotations_off = None
        self.class_data_off  = None
        self.static_values_off = None

class DexCallSiteId:
    def __init__(self):
        self.call_site_off   = None

class DexMethodHandle:
    def __init__(self):
        self.method_handle_type = None
        self.unused          = None
        self.field_or_method_id = None
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