# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_16-01.57.30 176069
# Run by LYF on Tue Sep 19 16:29:57 2023
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=606.0, 
    height=291.972229003906)
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
main_folder = r"D:\abaqus2022\temp\righteye\Search-Initial-Configuration\2D-Debug"  # set your own working directory
Step2_name = 'Step-2-' + str(status_code) + '.odb'
os.chdir(main_folder)
session.openOdb(os.path.join(main_folder,Step2_name))
odb = session.odbs[Step2_name]
p = mdb.models['Model-1'].PartFromOdb(name='Part-1', instance='PART-1-1', 
    odb=odb, shape=DEFORMED, step=0, frame=1)
#: The part "Part-1" has been imported from the mesh of part instance "PART-1-1" on the output database.
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
odb.close()
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((100.0, 0.3), ))
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', 
    material='Material-1', thickness=None)
#: Warning: Cannot continue yet--complete the step or cancel the procedure.
p = mdb.models['Model-1'].parts['Part-1']
e = p.elements
elements = e.getSequenceFromMask(mask=('[#ffffffff:4 #3fffff ]', ), )
p.Set(elements=elements, name='Material_Assign')
#: The set 'Material_Assign' has been created (150 elements).
p = mdb.models['Model-1'].parts['Part-1']
region = p.sets['Material_Assign']
p = mdb.models['Model-1'].parts['Part-1']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByThreePoints(coordSysType=CYLINDRICAL, origin=(0.0, 0.0, 0.0), 
    point1=(1.0, 0.0, 0.0), point2=(0.0, 0.0, -1.0))
p = mdb.models['Model-1'].parts['Part-1']
a.Instance(name='Part-1-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', nlgeom=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['Part-1-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=('[#ffffffc0 #ffffffff:4 #fffff ]', ), )
a.Set(nodes=nodes1, name='allnodes')
#: The set 'allnodes' has been created (174 nodes).
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['Part-1-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=('[#3f #0:4 #3f00000 ]', ), )
a.Set(nodes=nodes1, name='fixnode')
#: The set 'fixnode' has been created (12 nodes).
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['Part-1-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=(
    '[#20820820 #8208208 #82082082 #20820820 #8208208 #2082082 ]', ), )
a.Set(nodes=nodes1, name='loadnode')
#: The set 'loadnode' has been created (31 nodes).
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-1-1'].elements
face2Elements1 = f1.getSequenceFromMask(mask=(
    '[#21084210 #8421084 #42108421 #10842108 #210842 ]', ), )
a.Surface(face2Elements=face2Elements1, name='loadsurf')
#: The surface 'loadsurf' has been created (30 mesh edges).
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
a = mdb.models['Model-1'].rootAssembly
region = a.surfaces['loadsurf']
mdb.models['Model-1'].Pressure(name='Load-1', createStepName='Step-1', 
    region=region, distributionType=UNIFORM, field='', magnitude=10.0, 
    amplitude=UNSET)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['fixnode']
mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Step-1', 
    region=region, localCsys=None)
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