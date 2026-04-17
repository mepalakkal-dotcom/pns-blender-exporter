import os
import sys

# Add bundled lib path
lib_path = os.path.join(os.path.dirname(__file__), "lib")
if lib_path not in sys.path:
    sys.path.append(lib_path)

import polyhedral_net_splines as pns


def run_pns(input_obj, output_igs):
    # Minimal pipeline (depends on binding API)
    mesh = pns.load_obj(input_obj)
    patches = pns.build_patches(mesh)
    pns.write_iges(output_igs, patches)