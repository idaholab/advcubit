""" Basic example file for advcubit
"""

# import the package
import advcubit
# initialize advcubit
advcubit.init()

# start cubit
advcubit.startCubit()
# create a simple brick
brick = advcubit.brick(1, 1, 1)
# find top surface
topSurface = advcubit.findSurfaceWithNormal(brick.surfaces(), (0, 0, 1), 0)[0]
# apply scheme
advcubit.setMeshScheme(topSurface, advcubit.SurfaceMeshSchemes.tri)
# mesh surface
advcubit.mesh(topSurface)
# set volume mesh scheme
advcubit.setMeshScheme(brick, advcubit.VolumeMeshSchemes.sweep)
# mesh volume
advcubit.mesh(brick)
# create block
advcubit.createBlock(brick, 1)
# name block
advcubit.nameBlock(1, 'mein_block')
# set second order mesh
advcubit.setElementType(1, advcubit.VolumeElementTypes.WEDGE15)
# export to exodus
advcubit.export('basic.e', True)
# close cubit
advcubit.closeCubit()

# clean up cubit's mess
advcubit.deleteJournalFiles()
