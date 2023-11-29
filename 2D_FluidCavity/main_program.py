# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 21:08:33 2022

@author: Asuka
"""

import os
import numpy as np
import pandas as pd
import time
import subprocess
from IdentifyInitialConfiguration import *

main_folder = r"F:\LYF\FC-InitialConfiguration\RightEye_axi"  # set your own working directory

# node_num = 4283
max_loop_times = 1000
loop_time = 0

# read initial disp from step-1-0
subprocess.Popen('abaqus job={} cpus=32 gpus=32 int'.format('Step-1'),shell=True)  # submit job for step-1
status_filename = 'Step-1'
status_code = 0
time.sleep(20)
while status_code == 0:
    time.sleep(5)
    status_code = check_sta(status_filename)  # check whether the job is done
initial_step1_name = 'Step-1.dat'
print('The Step 1 procedure has been done !!!')
# with open(os.path.join(main_folder,initial_step1_name)) as initial_step1:
#     lines = initial_step1.readlines()
#     count = 0
#     for line in lines:
#         if '   THE FOLLOWING TABLE IS PRINTED FOR NODES BELONGING TO NODE SET ASSEMBLY_ALLNODES' in line:
#             node_output_start_line = count + 5
#         if 'THE ANALYSIS HAS BEEN COMPLETED' in line:
#             node_output_end_line = count - 8
#         count = count + 1
#     node_num = node_output_end_line - node_output_start_line
#     for i in range(node_num):
#         temp_line = lines[node_output_start_line+i].split()
#         dis_line = []
#         for j in range(len(temp_line)):
#             if j == 0:
#                 dis_line.append(int(temp_line[j]))
#             if j > 0:
#                 dis_line.append(float(temp_line[j]))
#         dis_list.append(dis_line)
#         dis_data = np.array(dis_list)

dis_data, node_num = dis_info(os.path.join(main_folder, initial_step1_name))  # read displacement field for step-1
Pend_aqu, Pend_vit = FC_info(os.path.join(main_folder,initial_step1_name))
initial_NodesInfo = ObtainNodeInfo(os.path.join(main_folder, 'Step-1.inp'))  # read all initial node info for some part
initial_Nodes = np.array(initial_NodesInfo)
initial_Nodes[:,0] = initial_Nodes[:,0] + 2         # convert to GLOBAL NODE number
initial_X0 = EffectiveNodes(initial_Nodes, dis_data[:,0])  # read initial node info for set "allnodes"
X0 = np.array(initial_X0)[:,1:]  # initial node info for set "allnodes" without nodelabel
P_penalty = 100
Ptarget = 1.706526316
Pstart_aqu = Ptarget
Pstart_vit = Ptarget
Pstart_aqu = Pstart_aqu - P_penalty*(Pend_aqu - Ptarget)
Pstart_vit = Pstart_vit - P_penalty*(Pend_vit - Ptarget)
with open('P_aqu.txt','w') as P_aqu:
    P_aqu.writelines(str(Pstart_aqu))
with open('P_vit.txt','w') as P_vit:
    P_vit.writelines(str(Pstart_vit))

relative_tol = 0.001
absolute_tol = 1e-4
implement_dis = np.zeros((node_num,3))  # 3 for 2D models
implement_dis[:,0] = dis_data[:,0]
implement_dis[:,1:] = -dis_data[:,1:]
last_dis = np.zeros((node_num,3))  # 3 for 2D models
last_dis[:,0] = dis_data[:,0]
last_dis[:,1:] = -dis_data[:,1:]
penalty = 1.00
        
while  loop_time<1 or disp_magnitude(Xn, X0).max()>absolute_tol or abs(Pend_aqu-Ptarget)>absolute_tol or abs(Pend_vit-Ptarget)>absolute_tol:

    with open('Step3_loop.txt','w') as step3Loop:
        step3Loop.writelines(str(loop_time))
    step3Loop.close()
    
    disp_sub_name = 'adjust_disp_' + str(loop_time) + '.for'
    WriteNewDisp(disp_sub_name, implement_dis)  # write DISP based on implement_dis
    step2_job_name = 'Step-2-' + str(loop_time)
    # create and submit job for Step-2.inp
    subprocess.Popen('abaqus job={} inp={} user={} cpus=32 gpus=32 int'.format(step2_job_name,'Step-2',disp_sub_name),shell=True)
    status_code = 0
    status_filename = 'Step-2-' + str(loop_time)
    time.sleep(20)
    while status_code == 0:
        time.sleep(5)
        status_code = check_sta(status_filename)
        # with open(status_filename,'r') as f:
            # status_code = int(f.read())
    print('The Step 2 at loop %d procedure has been done !!!'%loop_time)
    subprocess.Popen('abaqus cae nogui={}'.format('GenerateStep3_2D.py'),shell=True)
    step3_code = 0
    status_filename = 'Step-3.txt'
    time.sleep(20)
    while status_code == 0:
        time.sleep(5)
        with open(status_filename,'r') as f:
            status_code = int(f.read())  # check if GenerateStep3_2D.py has been done
    
    step3_inp_name = 'Step-3-' + str(loop_time) + '.inp'
    AddNodePrint(step3_inp_name)
    last_NodeInfo = ObtainNodeInfo(step3_inp_name)
    last_Nodes = np.array(last_NodeInfo)
    last_Nodes[:,0] = last_Nodes[:,0] + 2
    last_effective_Nodes = EffectiveNodes(last_Nodes, dis_data[:,0])
    subprocess.Popen('abaqus job={} cpus=32 gpus=32 int'.format(step3_inp_name[0:-4]),shell=True)
    status_code = 0 
    status_filename = 'Step-3-' + str(loop_time)
    while status_code == 0:
        time.sleep(5)
        status_code = check_sta(status_filename)
        # with open(status_filename,'r') as f:
        #     status_code = int(f.read())
    step3_data_name = 'Step-3-' + str(loop_time) + '.dat'
    print('The Step 3 at loop %d procedure has been done !!!'%loop_time)
    dis_data, _ = dis_info(step3_data_name)
    
    # generate new FC pressure
    Pend_aqu, Pend_vit = FC_info(step3_data_name)
    Pstart_aqu = Pstart_aqu - P_penalty*(Pend_aqu - Ptarget)
    Pstart_vit = Pstart_vit - P_penalty*(Pend_vit - Ptarget)
    with open('P_aqu.txt','w') as P_aqu:
        P_aqu.writelines(str(Pstart_aqu))
    with open('P_vit.txt','w') as P_vit:
        P_vit.writelines(str(Pstart_vit))
    
    Xn = last_effective_Nodes[:,1:] + dis_data[:,1:]
    implement_dis = np.zeros((node_num,3))  # 3 for 2D models
    implement_dis[:,0] = dis_data[:,0]
    # implement_dis[:,1:] = -(Xn - last_effective_Nodes[:,1:] - (Xn - X0))*penalty
    implement_dis[:,1:] = -dis_data[:,1:]*penalty
    loop_time = loop_time + 1
    print('The max error of displacement field is %8.10f. '%disp_magnitude(Xn, X0).max())
    print(f'Aqueous pressure error is {Pend_aqu-Ptarget}')
    print(f'Vitreous pressure error is {Pend_vit-Ptarget}')