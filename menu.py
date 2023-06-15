import nuke
nuke.tprint('Loading freezeSplineWarp_v3.py')
try:
    from freezeSplineWarp_v3 import *
except:
    pass

#===============================================================================
# BVFX ToolBar Menu definitions
#===============================================================================
toolbar = nuke.menu("Nodes")
bvfxt = toolbar.addMenu("BoundaryVFX Tools", "BoundaryVFX.png")
bvfxt.addCommand('FreezeWarp for Nuke', 'freezeWarp_v3()','shift+F8', icon='bvfx_SplineF.png')
