# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_16-01.57.30 176069
# Run by LYF on Mon Oct 23 22:32:44 2023
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=606.0, 
    height=308.583343505859)
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
main_folder = r"F:\LYF\FC-InitialConfiguration\RightEye_axi"  # set your own working directory
Step2_name = 'Step-2-' + str(status_code) + '.odb'
os.chdir(main_folder)

with open('P_aqu.txt','r') as P_aqu:
    Pstart_aqu = float(P_aqu.readline())
with open('P_vit.txt','r') as P_vit:
    Pstart_vit = float(P_vit.readline())

session.openOdb(os.path.join(main_folder,Step2_name))
odb = session.odbs[Step2_name]
p = mdb.models['Model-1'].PartFromOdb(name='RightEye_axi', 
    instance='RIGHTEYE_AXI-1', odb=odb, shape=DEFORMED, step=0, frame=1)
#: The part "RightEye_axi" has been imported from the mesh of part instance "RIGHTEYE_AXI-1" on the output database.
p = mdb.models['Model-1'].parts['RightEye_axi']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
odb.close()
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.openAuxMdb(pathName=os.path.join(main_folder,'RightEye_quarter.cae'))
mdb.copyAuxMdbModel(fromName='RightEye_axi', toName='Model_material')
mdb.closeAuxMdb()
import part
import assembly
import material
import section
import interaction
mdb.models['Model-1'].copyMaterials(sourceModel=mdb.models['Model_material'])
mdb.models['Model-1'].copySections(sourceModel=mdb.models['Model_material'])
mdb.models['Model-1'].copyInteractionProperties(
    sourceModel=mdb.models['Model_material'])
p = mdb.models['Model-1'].parts['RightEye_axi']
region = p.sets['SET-CILIARY']
p = mdb.models['Model-1'].parts['RightEye_axi']
p.SectionAssignment(region=region, sectionName='ciliary', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['RightEye_axi']
region = p.sets['SET-EPITH']
p = mdb.models['Model-1'].parts['RightEye_axi']
p.SectionAssignment(region=region, sectionName='epith', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['RightEye_axi']
region = p.sets['SET-LENS']
p = mdb.models['Model-1'].parts['RightEye_axi']
p.SectionAssignment(region=region, sectionName='lens', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['RightEye_axi']
region = p.sets['SET-SCLERA']
p = mdb.models['Model-1'].parts['RightEye_axi']
p.SectionAssignment(region=region, sectionName='sclera', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['RightEye_axi']
region = p.sets['SET-STROMA']
p = mdb.models['Model-1'].parts['RightEye_axi']
p.SectionAssignment(region=region, sectionName='stroma', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByThreePoints(coordSysType=CYLINDRICAL, origin=(0.0, 0.0, 0.0), 
    point1=(1.0, 0.0, 0.0), point2=(0.0, 0.0, -1.0))
p = mdb.models['Model-1'].parts['RightEye_axi']
a.Instance(name='RightEye_axi-1', part=p, dependent=ON)
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['RightEye_axi-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=('[#ffffffff:328 #3ff ]', ), )
a.Set(nodes=nodes1, name='allnodes')
#: The set 'allnodes' has been created (10506 nodes).
a = mdb.models['Model-1'].rootAssembly
a.ReferencePoint(point=(0.0, 12.3, 0.0))
a = mdb.models['Model-1'].rootAssembly
a.ReferencePoint(point=(0.0, 0.0, 0.0))
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[5], )
a.Set(referencePoints=refPoints1, name='FC_aqueous')
#: The set 'FC_aqueous' has been created (1 reference point).
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[6], )
a.Set(referencePoints=refPoints1, name='FC_vitreous')
#: The set 'FC_vitreous' has been created (1 reference point).
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', nlgeom=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
regionDef=mdb.models['Model-1'].rootAssembly.sets['FC_aqueous']
mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-2', 
    createStepName='Step-1', variables=('PCAV', 'CVOL'), region=regionDef, 
    sectionPoints=DEFAULT, rebar=EXCLUDE)
regionDef=mdb.models['Model-1'].rootAssembly.sets['FC_vitreous']
mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-3', 
    createStepName='Step-1', variables=('PCAV', 'CVOL'), region=regionDef, 
    sectionPoints=DEFAULT, rebar=EXCLUDE)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
a = mdb.models['Model-1'].rootAssembly
region1=a.sets['FC_aqueous']
a = mdb.models['Model-1'].rootAssembly
region2=a.instances['RightEye_axi-1'].surfaces['FC_AQUEOUS']
mdb.models['Model-1'].FluidCavity(name='FC_aqueous', createStepName='Initial', 
    cavityPoint=region1, cavitySurface=region2, 
    interactionProperty='aqueous-FC')
#: The interaction "FC_aqueous" has been created.
a = mdb.models['Model-1'].rootAssembly
region1=a.sets['FC_vitreous']
a = mdb.models['Model-1'].rootAssembly
region2=a.instances['RightEye_axi-1'].surfaces['FC_VITREOUS']
mdb.models['Model-1'].FluidCavity(name='FC_vitreous', createStepName='Initial', 
    cavityPoint=region1, cavitySurface=region2, 
    interactionProperty='vitreous-FC')
#: The interaction "FC_vitreous" has been created.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['RightEye_axi-1'].sets['SET-AXIS']
mdb.models['Model-1'].DisplacementBC(name='axi_fix', createStepName='Initial', 
    region=region, u1=SET, u2=UNSET, ur3=UNSET, amplitude=UNSET, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['RightEye_axi-1'].sets['SET-BOUNDARY']
mdb.models['Model-1'].DisplacementBC(name='fix', createStepName='Initial', 
    region=region, u1=UNSET, u2=SET, ur3=UNSET, amplitude=UNSET, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
mdb.models['Model-1'].FluidCavityPressure(name='FC_aqueous', 
    fluidCavity='FC_aqueous', fluidPressure=Pstart_aqu)
mdb.models['Model-1'].FluidCavityPressure(name='FC_vitreous', 
    fluidCavity='FC_vitreous', fluidPressure=Pstart_vit)
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
#: The job input file has been written to "Step-3.inp".

# flag for .py file completion
step3_status = 1
step3_status_filename = 'step3.txt'
with open(step3_status_filename,'w') as step3_status_file:
    step3_status_file.writelines(str(step3_status))
step3_status_file.close()