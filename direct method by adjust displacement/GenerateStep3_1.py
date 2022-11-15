# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_16-01.57.30 176069
# Run by Asuka on Mon Nov 14 10:21:38 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=380.390594482422, 
    height=191.722213745117)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
#: Executing "onCaeStartup()" in the site directory ...
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
import os
import time
with open('Step3_loop.txt','r') as f:
    status_code = int(f.read())
new_Step3_filename = 'Step-3-' + str(status_code)
f.close()
main_folder = r"I:/model debug/SearchInitialConfiguration"
Step2_name = 'Step-2-' + str(status_code) + '.odb'
os.chdir(main_folder)
session.openOdb(os.path.join(main_folder,Step2_name))
#: Model: I:/model debug/SearchInitialConfiguration/Step-2-0.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          5
#: Number of Steps:              1
odb = session.odbs[os.path.join(main_folder,Step2_name)]
p = mdb.models['Model-1'].PartFromOdb(name='cylinder-1', instance='CYLINDER-1', 
    odb=odb, shape=DEFORMED, step=0, frame=1)
#: The part "cylinder-1" has been imported from the mesh of part instance "CYLINDER-1" on the output database.
p = mdb.models['Model-1'].parts['cylinder-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
odb.close()
session.viewports['Viewport: 1'].view.setValues(nearPlane=86.1182, 
    farPlane=164.214, width=136.308, height=71.2224, viewOffsetX=15.4802, 
    viewOffsetY=0.781508)
session.viewports['Viewport: 1'].view.setValues(nearPlane=81.3077, 
    farPlane=136.163, width=128.694, height=67.244, cameraPosition=(-3.3925, 
    -4.25349, 124.388), cameraUpVector=(-0.6477, 0.633767, -0.422876), 
    cameraTarget=(0.752178, -17.2074, -0.0372362), viewOffsetX=14.6155, 
    viewOffsetY=0.737854)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((1.0, 0.35), ))
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', 
    material='Material-1', thickness=None)
p = mdb.models['Model-1'].parts['cylinder-1']
region = p.sets['SET-1']
p = mdb.models['Model-1'].parts['cylinder-1']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].view.setValues(nearPlane=78.6978, 
    farPlane=138.774, width=180.56, height=94.3447, viewOffsetX=25.4944, 
    viewOffsetY=3.55109)
session.viewports['Viewport: 1'].view.setValues(nearPlane=88.928, 
    farPlane=173.912, width=204.032, height=106.609, cameraPosition=(95.2722, 
    52.5038, 92.3075), cameraUpVector=(-0.848492, 0.529203, 0.00249599), 
    cameraTarget=(4.55241, -13.8513, 37.2297), viewOffsetX=28.8085, 
    viewOffsetY=4.01271)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['cylinder-1']
a.Instance(name='cylinder-1-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=92.1998, 
    farPlane=159.099, width=83.6195, height=43.692, cameraPosition=(73.978, 
    33.2153, 110.346), cameraUpVector=(-0.486763, 0.798108, -0.355084), 
    cameraTarget=(0.59201, -1.63039, 15.1267))
session.viewports['Viewport: 1'].view.setValues(nearPlane=91.5072, 
    farPlane=159.791, width=99.9193, height=52.2089, viewOffsetX=6.68969, 
    viewOffsetY=-2.35893)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', 
    maxNumInc=1000, minInc=1e-10)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=99.447, 
    farPlane=164.131, width=108.589, height=56.7389, cameraPosition=(124.056, 
    33.1385, 42.8941), cameraUpVector=(-0.57755, 0.815031, -0.0464708), 
    cameraTarget=(6.06245, -0.6808, 18.3935), viewOffsetX=7.27013, 
    viewOffsetY=-2.56361)
session.viewports['Viewport: 1'].view.setValues(nearPlane=101.992, 
    farPlane=163.909, width=111.368, height=58.1908, cameraPosition=(127.864, 
    34.4232, 21.9768), cameraUpVector=(-0.580396, 0.814303, -0.00718928), 
    cameraTarget=(7.63076, -0.0764043, 17.4673), viewOffsetX=7.45616, 
    viewOffsetY=-2.62921)
session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=94.9397, 
    farPlane=142.817, width=81.3528, height=42.5077, viewOffsetX=-0.523896, 
    viewOffsetY=-1.49589)
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].view.setValues(nearPlane=92.6136, 
    farPlane=145.143, width=115.285, height=60.2376, cameraPosition=(-119.182, 
    -4.67331, 14.9969), cameraTarget=(-0.303886, -4.67331, 14.9969))
session.viewports['Viewport: 1'].view.setValues(nearPlane=91.0008, 
    farPlane=147.193, cameraPosition=(-118.973, -10.8515, 11.6067), 
    cameraUpVector=(-0.0520755, 0.998639, 0.00295849))
session.viewports['Viewport: 1'].view.setValues(nearPlane=91.3767, 
    farPlane=146.399, cameraPosition=(-119.066, -5.27212, 9.76453), 
    cameraUpVector=(-0.00539248, 0.999967, 0.00601511), cameraTarget=(
    -0.304056, -4.66307, 14.9935))
session.viewports['Viewport: 1'].view.setValues(nearPlane=91.7839, 
    farPlane=145.933, cameraPosition=(-119.166, -4.24595, 13.0805), 
    cameraUpVector=(0.00352146, 0.999994, -0.000771717), cameraTarget=(
    -0.304064, -4.66299, 14.9938))
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['cylinder-1-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=(
    '[#ffffa6c9 #fff80007 #ffffffff #fe0001ff #3fffffff #ffffffff #fff80007', 
    ' #3fffff #ff000080 #7ffffff #fffff800 #ffff7fff #ffff0000:2 #ffffffff:19', 
    ' #ffff0000 #ffffffff:19 #3fffff #ffffffc0 #ffffffff:19 #1ffffff #fffffe00', 
    ' #ffffffff:18 #fffffff #fffff000 #ffffffff:37 #fffffff ]', ), )
a.Set(nodes=nodes1, name='allnodes')
#: The set 'allnodes' has been created (4080 nodes).
session.viewports['Viewport: 1'].view.setValues(nearPlane=87.7125, 
    farPlane=149.834, cameraPosition=(-110.976, -4.79632, -28.4032), 
    cameraUpVector=(-0.0110943, 0.99962, 0.0252167), cameraTarget=(-0.305436, 
    -4.6629, 15.0007))
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['cylinder-1-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=(
    '[#5936 #7fff8 #0 #1fffe00 #c0000000 #0 #7fff8', 
    ' #ffc00000 #ffff7f #f8000000 #7ff #8000 #ffff:2 #0:19', 
    ' #ffff #0:19 #ffc00000 #3f #0:19 #fe000000 #1ff', 
    ' #0:18 #f0000000 #fff ]', ), )
a.Set(nodes=nodes1, name='fixnode')
#: The set 'fixnode' has been created (204 nodes).
session.viewports['Viewport: 1'].view.setValues(nearPlane=85.3446, 
    farPlane=152.201, width=157.084, height=82.0783, cameraPosition=(-112.937, 
    3.30897, -23.4268), cameraTarget=(-2.26691, 3.44239, 19.9771))
session.viewports['Viewport: 1'].view.setValues(nearPlane=87.6289, 
    farPlane=152.499, cameraPosition=(-119.589, 6.34433, 1.04622), 
    cameraUpVector=(0.0301352, 0.998983, -0.0335273), cameraTarget=(-2.26103, 
    3.43971, 19.9555))
session.viewports['Viewport: 1'].view.setValues(nearPlane=84.4702, 
    farPlane=162.442, cameraPosition=(-78.271, -29.3323, 106.088), 
    cameraUpVector=(-0.377622, 0.92586, 0.0136149), cameraTarget=(-1.85271, 
    3.08714, 20.9936))
session.viewports['Viewport: 1'].view.setValues(nearPlane=91.3771, 
    farPlane=158.615, cameraPosition=(-23.0074, -24.0639, 135.42), 
    cameraUpVector=(-0.481932, 0.869145, 0.11104), cameraTarget=(0.196887, 
    3.28253, 22.0814))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
a = mdb.models['Model-1'].rootAssembly
region = a.sets['fixnode']
mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Initial', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].view.setValues(width=167.111, height=87.3173, 
    cameraPosition=(-20.7581, -21.4327, 136.515), cameraTarget=(2.4462, 
    5.91375, 23.1768))
session.viewports['Viewport: 1'].view.setValues(nearPlane=94.8745, 
    farPlane=165.383, cameraPosition=(39.7588, 32.1326, 134.407), 
    cameraUpVector=(-0.687851, 0.723459, 0.0588911), cameraTarget=(5.40844, 
    8.53571, 23.0736))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
mdb.models['Model-1'].TabularAmplitude(name='Amp-1', timeSpan=STEP, 
    smooth=SOLVER_DEFAULT, data=((0.0, 0.0), (1.0, 1.0)))
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['cylinder-1-1'].elements
face2Elements1 = f1.getSequenceFromMask(mask=(
    '[#ffffffff:10 #fffff #0:10 #ffffff00 #ffffffff:9 #fffffff #0:10', 
    ' #ffff0000 #ffffffff:10 #f #0:9 #ff000000 #ffffffff:10 #fff ]', ), )
region = a.Surface(face2Elements=face2Elements1, name='Surf-1')
mdb.models['Model-1'].Pressure(name='Load-1', createStepName='Step-1', 
    region=region, distributionType=UNIFORM, field='', magnitude=0.005, 
    amplitude='Amp-1')
session.viewports['Viewport: 1'].view.setValues(nearPlane=93.2646, 
    farPlane=166.993, width=201.197, height=105.128, cameraPosition=(43.9573, 
    39.9193, 131.461), cameraTarget=(9.60698, 16.3224, 20.1278))
session.viewports['Viewport: 1'].view.setValues(nearPlane=77.4855, 
    farPlane=165.395, cameraPosition=(69.5388, -64.533, 91.8097), 
    cameraUpVector=(-0.463463, 0.434912, 0.772045), cameraTarget=(11.8188, 
    7.29135, 16.6995))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
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