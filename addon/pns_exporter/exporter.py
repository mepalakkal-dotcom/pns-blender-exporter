import bpy
import tempfile
import os
from .core import run_pns


class EXPORT_OT_pns(bpy.types.Operator):
    bl_idname = "export_scene.pns_iges"
    bl_label = "Export PolySpline IGES"

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        obj = context.active_object

        if obj.type != 'MESH':
            self.report({'ERROR'}, "Select a mesh")
            return {'CANCELLED'}

        tmp = tempfile.mktemp(suffix=".obj")

        bpy.ops.wm.obj_export(
            filepath=tmp,
            export_selected_objects=True
        )

        try:
            run_pns(tmp, self.filepath)
        except Exception as e:
            self.report({'ERROR'}, str(e))
            return {'CANCELLED'}

        self.report({'INFO'}, "Exported successfully")
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}