bl_info = {
    "name": "PolySpline NURBS Exporter",
    "author": "Jaseel",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "category": "Import-Export",
}

import bpy
from .exporter import EXPORT_OT_pns

def menu_func(self, context):
    self.layout.operator(EXPORT_OT_pns.bl_idname, text="PolySpline IGES (.igs)")

def register():
    bpy.utils.register_class(EXPORT_OT_pns)
    bpy.types.TOPBAR_MT_file_export.append(menu_func)

def unregister():
    bpy.types.TOPBAR_MT_file_export.remove(menu_func)
    bpy.utils.unregister_class(EXPORT_OT_pns)