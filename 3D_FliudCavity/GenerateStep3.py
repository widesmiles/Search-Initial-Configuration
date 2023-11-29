# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_16-01.57.30 176069
# Run by LYF on Sat Oct 21 14:02:58 2023
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=606.0, 
    height=344.0)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()

import os
import time
with open('Step3_loop.txt','r') as f:
    status_code = int(f.read())
new_Step3_filename = 'Step-3-' + str(status_code)
f.close()
main_folder = r"F:\LYF\FC-InitialConfiguration\Debug" # Set your own work directory
Step2_name = 'Step-2-' + str(status_code) + '.odb'
os.chdir(main_folder)

with open('P_FC.txt','r') as P_FC:
    Pstart = float(P_FC.readline())

session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.openOdb(os.path.join(main_folder,Step2_name))
odb = session.odbs[Step2_name]
p = mdb.models['Model-1'].PartFromOdb(name='Part-1', instance='PART-1-1', 
    odb=odb, shape=DEFORMED, step=0, frame=-1)
#: The part "Part-1" has been imported from the mesh of part instance "PART-1-1" on the output database.
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
odb.close()
set1 = mdb.models['Model-1'].parts['Part-1'].sets['MATER_ASSIGN']
leaf = dgm.LeafFromSets(sets=(set1, ))
session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.meshEditOptions.setValues(enableUndo=True, maxUndoCacheElements=0.5)
# p = mdb.models['Model-1'].parts['Part-1']
# e = p.elements
# elements = e.getSequenceFromMask(mask=('[#0:46 #f0000000 #ffffffff:9 #ff ]', ), 
#     )
# p.deleteElement(elements=elements)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].partDisplay.displayGroup.add(leaf=leaf)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((200.0, 0.3), ))
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', 
    material='Material-1', thickness=None)
p = mdb.models['Model-1'].parts['Part-1']
e = p.elements
elements = e.getSequenceFromMask(mask=('[#ffffffff:46 #fffffff ]', ), )
region = regionToolset.Region(elements=elements)
p = mdb.models['Model-1'].parts['Part-1']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39.2078, 
    farPlane=70.1216, width=36.51, height=18.3988, cameraPosition=(-28.5309, 
    25.8572, 44.2911), cameraUpVector=(0.493705, 0.767425, -0.409041), 
    cameraTarget=(7.81519, 6.87108, 7.8152))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a1 = mdb.models['Model-1'].rootAssembly
a1.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Part-1']
a1.Instance(name='Part-1-1', part=p, dependent=ON)
a = mdb.models['Model-1'].rootAssembly
a.ReferencePoint(point=(0.0, 0.0, 0.0))
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['Part-1-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=('[#ffffffff:62 #3 ]', ), )
a.Set(nodes=nodes1, name='allnodes')
#: The set 'allnodes' has been created (1986 nodes).
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[4], )
a.Set(referencePoints=refPoints1, name='FC')
#: The set 'FC' has been created (1 reference point).
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', nlgeom=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
mdb.models['Model-1'].FluidCavityProperty(name='IntProp-1', fluidDensity=1e-09, 
    useBulkModulus=True, bulkModulusTable=((2000.0, ), ))
#: The interaction property "IntProp-1" has been created.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[4], )
region1=regionToolset.Region(referencePoints=refPoints1)
a = mdb.models['Model-1'].rootAssembly
region2=a.instances['Part-1-1'].surfaces['FCSURFACE']
mdb.models['Model-1'].FluidCavity(name='FC', createStepName='Initial', 
    cavityPoint=region1, cavitySurface=region2, 
    interactionProperty='IntProp-1')
#: The interaction "FC" has been created.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38.8852, 
    farPlane=70.3585, width=36.2096, height=18.2474, cameraPosition=(-19.4623, 
    35.0771, 46.1865), cameraUpVector=(-0.231101, 0.358412, -0.904507), 
    cameraTarget=(7.81519, 6.87108, 7.8152))
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['Part-1-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=(
    '[#c004c566 #7f #800007fc #f00003ff #100001f #c0000000 #7ff', 
    ' #1ffc00 #0:6 #1ff00 #0:5 #7fc000 #0:5 #fff00000', 
    ' #3f #0:3 #7fffe000 ]', ), )
region = regionToolset.Region(nodes=nodes1)
mdb.models['Model-1'].XsymmBC(name='xsym', createStepName='Initial', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.83, 
    farPlane=69.8293, width=38.0206, height=19.16, cameraPosition=(19.6343, 
    -21.2673, 53.1796), cameraUpVector=(-0.631078, 0.741491, 0.227885), 
    cameraTarget=(7.62919, 7.13913, 7.78193))
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['Part-1-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=(
    '[#1c3f00 #0:2 #7fc00 #ff803fe0 #200ff803 #0 #c0180000', 
    ' #1ffc01ff #0:11 #3fe0 #0:5 #ff800 #0:5 #fffe0000', ' #7 #0:4 #7fffe0 ]', 
    ), )
region = regionToolset.Region(nodes=nodes1)
mdb.models['Model-1'].YsymmBC(name='ysym', createStepName='Initial', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41.4381, 
    farPlane=69.1956, width=38.5868, height=19.4454, cameraPosition=(53.4621, 
    2.74893, 37.9131), cameraUpVector=(-0.670233, 0.558113, 0.489181), 
    cameraTarget=(7.90309, 7.33359, 7.65832))
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.8184, 
    farPlane=69.9489, width=38.0099, height=19.1546, cameraPosition=(45.4023, 
    15.8141, -32.018), cameraUpVector=(0.429741, 0.0869836, 0.898753), 
    cameraTarget=(7.83969, 7.43637, 7.1082))
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['Part-1-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=(
    '[#3ff17033 #fe000000 #40000003 #1 #0 #fff007fc #1800', 
    ' #3fe #1803fe00 #0:5 #3fe0000 #0:11 #7fc #0:3', 
    ' #7fffe00 #0:7 #ff800000 #1ff ]', ), )
region = regionToolset.Region(nodes=nodes1)
mdb.models['Model-1'].ZsymmBC(name='zsym', createStepName='Initial', 
    region=region, localCsys=None)
mdb.models['Model-1'].FluidCavityPressure(name='FC_pressure', fluidCavity='FC', 
    fluidPressure=Pstart)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name=new_Step3_filename, model='Model-1', description='', type=ANALYSIS,
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
        scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1,
        multiprocessingMode=DEFAULT, numCpus=8, numDomains=8, numGPUs=0)
mdb.jobs[new_Step3_filename].writeInput(consistencyChecking=OFF)
#: The job input file has been written to "Job-1.inp".

# flag for .py file completion
step3_status = 1
step3_status_filename = 'step3.txt'
with open(step3_status_filename,'w') as step3_status_file:
    step3_status_file.writelines(str(step3_status))
step3_status_file.close()