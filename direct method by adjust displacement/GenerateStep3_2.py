# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_16-01.57.30 176069
# Run by Asuka on Mon Nov 14 16:32:26 2022
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
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
import os
import time
with open('Step3_loop.txt','r') as f:
    status_code = int(f.read())
new_Step3_filename = 'Step-3-' + str(status_code)
f.close()
main_folder = r"E:\model debug\SearchInitialConfiguration"
Step2_name = 'Step-2-' + str(status_code) + '.odb'
os.chdir(main_folder)
session.openOdb(os.path.join(main_folder,Step2_name))
#: Model: I:/model debug/SearchInitialConfiguration/Step-2-43.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          6
#: Number of Steps:              1
odb = session.odbs[os.path.join(main_folder,Step2_name)]
p = mdb.models['Model-1'].PartFromOdb(name='cylinder', instance='CYLINDER-1', 
    odb=odb, shape=DEFORMED, step=0, frame=1)
#: The part "cylinder" has been imported from the mesh of part instance "CYLINDER-1" on the output database.
p = mdb.models['Model-1'].parts['cylinder']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
odb.close()
session.viewports['Viewport: 1'].view.setValues(nearPlane=82.6304, 
    farPlane=161.075, width=149.282, height=78.0015, viewOffsetX=9.50461, 
    viewOffsetY=3.84346)
session.viewports['Viewport: 1'].view.setValues(nearPlane=78.1157, 
    farPlane=157.167, width=141.126, height=73.7397, cameraPosition=(56.3754, 
    -89.0751, 68.2711), cameraUpVector=(-0.00401796, 0.857317, 0.514773), 
    cameraTarget=(-4.46468, -4.24415, 5.42024), viewOffsetX=8.9853, 
    viewOffsetY=3.63346)
session.viewports['Viewport: 1'].view.setValues(nearPlane=79.3646, 
    farPlane=146.78, width=143.382, height=74.9188, cameraPosition=(-13.7602, 
    -109.552, 43.4913), cameraUpVector=(0.0264784, 0.659071, 0.751614), 
    cameraTarget=(-3.02007, 3.12102, -1.64683), viewOffsetX=9.12896, 
    viewOffsetY=3.69155)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((1.0, 0.35), ))
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', 
    material='Material-1', thickness=None)
p = mdb.models['Model-1'].parts['cylinder']
region = p.sets['SET-1']
p = mdb.models['Model-1'].parts['cylinder']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].view.setValues(nearPlane=78.6124, 
    farPlane=147.532, width=160.733, height=83.9845, viewOffsetX=14.6855, 
    viewOffsetY=1.41398)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['cylinder']
a.Instance(name='cylinder-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=86.5096, 
    farPlane=157.195, width=89.1887, height=46.6021, viewOffsetX=4.25677, 
    viewOffsetY=-0.5317)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=91.8656, 
    farPlane=144.353, width=94.7106, height=49.4873, cameraPosition=(4.75765, 
    27.5998, 129.905), cameraUpVector=(-0.840868, 0.335282, -0.424885), 
    cameraTarget=(1.89568, -6.59971, 12.9848), viewOffsetX=4.52032, 
    viewOffsetY=-0.564619)
session.viewports['Viewport: 1'].view.setValues(nearPlane=84.8816, 
    farPlane=155.006, width=87.5103, height=45.7251, cameraPosition=(55.2129, 
    65.446, 99.3353), cameraUpVector=(-0.989968, 0.140359, 0.016181), 
    cameraTarget=(2.5475, -7.11116, 16.8129), viewOffsetX=4.17667, 
    viewOffsetY=-0.521694)
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', 
    maxNumInc=1000, minInc=1e-10)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=84.9291, 
    farPlane=154.958, width=99.0939, height=51.7776, viewOffsetX=8.56339, 
    viewOffsetY=-1.71132)
session.viewports['Viewport: 1'].view.setValues(nearPlane=96.5373, 
    farPlane=159.937, width=112.638, height=58.8546, cameraPosition=(121.6, 
    29.699, -14.2262), cameraUpVector=(-0.493745, 0.847569, 0.194533), 
    cameraTarget=(8.11219, 3.32154, 21.4505), viewOffsetX=9.73385, 
    viewOffsetY=-1.94523)
session.viewports['Viewport: 1'].view.setValues(nearPlane=98.1074, 
    farPlane=163.05, width=114.47, height=59.8118, cameraPosition=(90.1804, 
    18.376, -78.1596), cameraUpVector=(-0.493885, 0.860673, 0.123776), 
    cameraTarget=(11.1421, 6.97756, 13.8791), viewOffsetX=9.89216, 
    viewOffsetY=-1.97687)
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['cylinder-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=(
    '[#5936 #7fff8 #0 #1fffe00 #c0000000 #0 #7fff8', 
    ' #ffc00000 #ffff7f #f8000000 #7ff #8000 #ffff:2 #0:19', 
    ' #ffff #0:19 #ffc00000 #3f #0:19 #fe000000 #1ff', 
    ' #0:18 #f0000000 #fff ]', ), )
a.Set(nodes=nodes1, name='fixnode')
#: The set 'fixnode' has been created (204 nodes).
session.viewports['Viewport: 1'].view.setValues(nearPlane=95.229, 
    farPlane=158.268, width=111.112, height=58.057, cameraPosition=(106.784, 
    -4.01521, 84.2831), cameraUpVector=(-0.282, 0.95494, -0.0925515), 
    cameraTarget=(-1.28563, 1.17262, 28.2293), viewOffsetX=9.60194, 
    viewOffsetY=-1.91887)
session.viewports['Viewport: 1'].view.setValues(nearPlane=93.6132, 
    farPlane=159.58, width=109.227, height=57.0721, cameraPosition=(74.5402, 
    -15.4507, 116.921), cameraUpVector=(-0.243774, 0.967218, -0.0711597), 
    cameraTarget=(-6.15453, -0.420162, 26.8628), viewOffsetX=9.43902, 
    viewOffsetY=-1.88631)
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['cylinder-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=(
    '[#a6c9 #0 #3fffc0 #0 #3ffff000 #fff80000 #7', 
    ' #3fffc0 #80 #7fff800 #c0000000 #ffff7fff #ffff0000 #0:19', 
    ' #ffff0000 #0:21 #3fffc0 #0:19 #1fffe00 #0:20 #ffff000 ]', ), )
a.Set(nodes=nodes1, name='asymnode')
#: The set 'asymnode' has been created (204 nodes).
session.viewports['Viewport: 1'].view.setValues(nearPlane=96.5204, 
    farPlane=156.99, width=112.619, height=58.8447, cameraPosition=(115.965, 
    9.48605, 66.8019), cameraUpVector=(-0.334528, 0.921296, -0.198254), 
    cameraTarget=(0.64764, 3.33329, 27.916), viewOffsetX=9.73215, 
    viewOffsetY=-1.94489)
session.viewports['Viewport: 1'].view.setValues(nearPlane=98.3966, 
    farPlane=155.526, width=114.808, height=59.9885, cameraPosition=(125.205, 
    -11.3898, 36.6466), cameraUpVector=(-0.227734, 0.973005, -0.0373901), 
    cameraTarget=(4.39784, 1.73273, 27.6251), viewOffsetX=9.92132, 
    viewOffsetY=-1.98269)
session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=92.1487, 
    farPlane=139.568, width=89.9965, height=47.0241, viewOffsetX=2.9382, 
    viewOffsetY=-2.97347)
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].view.setValues(nearPlane=88.3681, 
    farPlane=150.231, cameraPosition=(37.7857, -113.218, 14.1874), 
    cameraUpVector=(0.577599, 0.22003, 0.786109))
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['cylinder-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=(
    '[#ffff0000 #fff80007 #ffc0003f #fe0001ff #fff #7ffff #fff80000', 
    ' #3f #ff000000 #7ff #3ffff800 #0:2 #ffff0000 #ffffffff:18', 
    ' #ffff #ffff0000 #ffffffff:19 #3fffff #ffc00000 #ffffffff:19 #1ff', 
    ' #fffffe00 #ffffffff:18 #fffffff #f0000000 #ffffffff:37 #fffffff ]', ), )
a.Set(nodes=nodes1, name='allnodes')
#: The set 'allnodes' has been created (3876 nodes).
session.viewports['Viewport: 1'].view.setValues(nearPlane=87.84, 
    farPlane=150.759, width=128.059, height=66.9119, cameraPosition=(42.536, 
    -111.648, 11.5635), cameraTarget=(4.75033, -2.16188, 8.68193))
session.viewports['Viewport: 1'].view.setValues(nearPlane=79.8073, 
    farPlane=154.242, cameraPosition=(81.3005, -43.416, 87.4545), 
    cameraUpVector=(0.284568, 0.927327, 0.243076), cameraTarget=(5.86844, 
    -0.193829, 10.8709))
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=76.3597, 
    farPlane=157.689, width=186.386, height=97.3889, cameraPosition=(94.7891, 
    -41.8326, 75.0624), cameraTarget=(19.357, 1.38958, -1.5212))
a = mdb.models['Model-1'].rootAssembly
region = a.sets['fixnode']
mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Step-1', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
mdb.models['Model-1'].boundaryConditions['BC-1'].move('Step-1', 'Initial')
a = mdb.models['Model-1'].rootAssembly
region = a.sets['asymnode']
mdb.models['Model-1'].EncastreBC(name='BC-2', createStepName='Initial', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73.7465, 
    farPlane=160.303, width=224.404, height=117.254, cameraPosition=(98.969, 
    -42.6117, 70.5056), cameraTarget=(23.537, 0.610448, -6.07803))
session.viewports['Viewport: 1'].view.setValues(nearPlane=88.3657, 
    farPlane=171.604, cameraPosition=(97.5736, -88.8545, -2.56644), 
    cameraUpVector=(0.469477, 0.427402, 0.772605), cameraTarget=(23.5231, 
    0.149671, -6.80614))
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