# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_16-01.57.30 176069
# Run by wides on Mon Nov 14 00:32:25 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=420.75, 
    height=267.0)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
import os
import time

with open('Step3_loop.txt','r') as f:
    status_code = int(f.read())
new_Step3_filename = 'Step-3-' + str(status_code)
f.close()
main_folder = r"E:/model debug/SearchInitialConfiguration"
Step2_name = 'Step-2-' + str(status_code) + '.odb'
os.chdir(main_folder)
session.openOdb(os.path.join(main_folder,Step2_name))
#: Model: E:/model debug/SearchInitialConfiguration/Step-2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          4
#: Number of Steps:              1
odb = session.odbs[os.path.join(main_folder,Step2_name)]
p = mdb.models['Model-1'].PartFromOdb(name='cylinder', instance='CYLINDER-1', 
    odb=odb, shape=DEFORMED, step=0, frame=1)
#: The part "cylinder" has been imported from the mesh of part instance "CYLINDER-1" on the output database.
p = mdb.models['Model-1'].parts['cylinder']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
odb.close()
session.viewports['Viewport: 1'].view.setValues(nearPlane=85.4585, 
    farPlane=158.307, width=84.478, height=55.5215, viewOffsetX=8.18329, 
    viewOffsetY=-0.363849)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((1.0, 0.35), ))
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', 
    material='Material-1', thickness=None)
p = mdb.models['Model-1'].parts['cylinder']
e = p.elements
elements = e.getSequenceFromMask(mask=('[#ffffffff:85 ]', ), )
region = p.Set(elements=elements, name='cylinder')
p = mdb.models['Model-1'].parts['cylinder']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['cylinder']
a.Instance(name='cylinder-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=83.9851, 
    farPlane=159.78, width=100.365, height=65.9627, viewOffsetX=4.39525, 
    viewOffsetY=1.04124)
session.viewports['Viewport: 1'].view.setValues(nearPlane=83.8362, 
    farPlane=155.052, width=100.187, height=65.8457, cameraPosition=(23.9179, 
    -80.35, 100.279), cameraUpVector=(-0.214198, 0.899007, 0.381976), 
    cameraTarget=(-1.24664, -2.69734, 9.76822), viewOffsetX=4.38746, 
    viewOffsetY=1.03939)
session.viewports['Viewport: 1'].view.setValues(nearPlane=84.7239, 
    farPlane=156.375, width=101.248, height=66.5432, cameraPosition=(26.9175, 
    -102.878, 72.013), cameraUpVector=(-0.14735, 0.753333, 0.640919), 
    cameraTarget=(-1.45132, -1.80734, 10.0827), viewOffsetX=4.43392, 
    viewOffsetY=1.0504)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', 
    maxNumInc=1000, minInc=1e-10)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=83.4582, 
    farPlane=157.641, width=120.079, height=78.9194, viewOffsetX=11.1216, 
    viewOffsetY=-1.85325)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].view.setValues(nearPlane=90.7702, 
    farPlane=160.505, width=130.599, height=85.8337, cameraPosition=(22.8247, 
    -118.833, -19.1968), cameraUpVector=(-0.140728, 0.0854954, 0.98635), 
    cameraTarget=(-1.53151, -2.65259, 8.44769), viewOffsetX=12.096, 
    viewOffsetY=-2.01561)
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['cylinder-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=(
    '[#5936 #7fff8 #0 #1fffe00 #c0000000 #0 #7fff8', 
    ' #ffc00000 #ffff7f #f8000000 #7ff #8000 #ffff:2 #0:19', 
    ' #ffff #0:19 #ffc00000 #3f #0:19 #fe000000 #1ff', 
    ' #0:18 #f0000000 #fff ]', ), )
region = a.Set(nodes=nodes1, name='Set-1')
nodes2 = n1.getSequenceFromMask(mask=('[#ffffffff:133 #fffffff ]', ), )
a.Set(nodes=nodes2, name='allnodes')
mdb.models['Model-1'].ZsymmBC(name='BC-1', createStepName='Initial', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=85.4465, 
    farPlane=157.762, width=122.939, height=80.7995, cameraPosition=(18.3076, 
    -113.048, 55.884), cameraUpVector=(0.158097, 0.640729, 0.751313), 
    cameraTarget=(-0.620519, 0.840839, 16.8163), viewOffsetX=11.3866, 
    viewOffsetY=-1.89739)
session.viewports['Viewport: 1'].view.setValues(nearPlane=76.0851, 
    farPlane=152.851, width=109.47, height=71.9472, cameraPosition=(-28.537, 
    -77.3196, 94.5421), cameraUpVector=(0.326847, 0.817968, 0.473391), 
    cameraTarget=(0.0335008, 8.32109, 12.6602), viewOffsetX=10.1391, 
    viewOffsetY=-1.68951)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
mdb.models['Model-1'].TabularAmplitude(name='Amp-1', timeSpan=STEP, 
    smooth=SOLVER_DEFAULT, data=((0.0, 0.0), (1.0, 1.0)))
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['cylinder-1'].elements
face2Elements1 = f1.getSequenceFromMask(mask=(
    '[#ffffffff:10 #fffff #0:10 #ffffff00 #ffffffff:9 #fffffff #0:10', 
    ' #ffff0000 #ffffffff:10 #f #0:9 #ff000000 #ffffffff:10 #fff ]', ), )
region = a.Surface(face2Elements=face2Elements1, name='Surf-1')
mdb.models['Model-1'].Pressure(name='Load-1', createStepName='Step-1', 
    region=region, distributionType=UNIFORM, field='', magnitude=0.005, 
    amplitude='Amp-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['cylinder']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=84.0502, 
    farPlane=159.715, width=100.033, height=65.9071, viewOffsetX=13.1279, 
    viewOffsetY=-4.45613)
mdb.meshEditOptions.setValues(enableUndo=True, maxUndoCacheElements=0.5)
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)


mdb.Job(name=new_Step3_filename, model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs[new_Step3_filename].writeInput(consistencyChecking=OFF)
#: The job input file has been written to "Step-3.inp".

step3_status = 1
step3_status_filename = 'step3.txt'
with open(step3_status_filename,'w') as step3_status_file:
    step3_status_file.writelines(str(step3_status))
step3_status_file.close()
