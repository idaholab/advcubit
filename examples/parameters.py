""" Example to show the use of the additional parameters
"""

# import and init advcubit
import advcubit
advcubit.init(None, False)

# start cubit
advcubit.startCubit()

# create a circle
circle = advcubit.createCircle(1)
# create a surface from circle
surface = advcubit.create_surface([circle]).surfaces()[0]

# set meshing scheme, use the additional parameters for advanced control
advcubit.setMeshScheme(surface, advcubit.SurfaceMeshSchemes.circle, fraction=0.5, interval=3)
# mesh surface
surface.mesh()
# sweep the surface, include the mesh using a parameter
body = advcubit.sweepVector(circle, (0, 0, -1), 'include_mesh')

# create block and export
advcubit.createBlock(body, 1)
advcubit.export('param.e')

# close cubit and clean
advcubit.closeCubit()
advcubit.deleteJournalFiles()
