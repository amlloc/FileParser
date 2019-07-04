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

class 