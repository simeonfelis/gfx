# generate code files
projectPath = "config/" + Variables.get("__CONFIGURATION_NAME") + "/gfx/driver/external_controller"

GFX_DRIVER_H = comp.createFileSymbol("GFX_DRIVER_H", None)
GFX_DRIVER_H.setSourcePath("../../templates/gfx_driver.h.ftl")
GFX_DRIVER_H.setDestPath("gfx/driver/")
GFX_DRIVER_H.setOutputName("gfx_driver.h")
GFX_DRIVER_H.setProjectPath(projectPath)
GFX_DRIVER_H.setType("HEADER")
GFX_DRIVER_H.setMarkup(True)

GFX_DRIVER_C = comp.createFileSymbol("GFX_DRIVER_C", None)
GFX_DRIVER_C.setSourcePath("../../templates/gfx_driver.c.ftl")
GFX_DRIVER_C.setDestPath("gfx/driver/")
GFX_DRIVER_C.setOutputName("gfx_driver.c")
GFX_DRIVER_C.setProjectPath(projectPath)
GFX_DRIVER_C.setType("SOURCE")
GFX_DRIVER_C.setMarkup(True)

GFX_EXTERNAL_CONTROLLER_C = comp.createFileSymbol("GFX_EXTERNAL_CONTROLLER_C", None)
GFX_EXTERNAL_CONTROLLER_C.setDestPath("gfx/driver/controller/external_controller")
GFX_EXTERNAL_CONTROLLER_C.setSourcePath("templates/drv_gfx_external_controller.c.ftl")
GFX_EXTERNAL_CONTROLLER_C.setOutputName("drv_gfx_external_controller.c")
GFX_EXTERNAL_CONTROLLER_C.setProjectPath(projectPath)
GFX_EXTERNAL_CONTROLLER_C.setType("SOURCE")
GFX_EXTERNAL_CONTROLLER_C.setMarkup(True)

GFX_EXTERNAL_CONTROLLER_H = comp.createFileSymbol("GFX_EXTERNAL_CONTROLLER_H", None)
GFX_EXTERNAL_CONTROLLER_H.setDestPath("gfx/driver/controller/external_controller/")
GFX_EXTERNAL_CONTROLLER_H.setSourcePath("templates/drv_gfx_external_controller.h.ftl")
GFX_EXTERNAL_CONTROLLER_H.setOutputName("drv_gfx_external_controller.h")
GFX_EXTERNAL_CONTROLLER_H.setProjectPath(projectPath)
GFX_EXTERNAL_CONTROLLER_H.setType("HEADER")
GFX_EXTERNAL_CONTROLLER_H.setMarkup(True)