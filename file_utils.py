# encoding:utf-8

import maya.cmds as cmds
from maya.OpenMaya import MGlobal

def exportObjectAsAssFile(location="", objectName=""):
    """
    export objects to ass file
    """
    if objectName == "":
        MGlobal.displayWarning("No object exported!!!")
        return False

    else:
        cmds.select(objectName, r=True)
        cmds.file(location + "/" + objectName, type="mayaBinary", force=True, exportSelected=True)
        return True
