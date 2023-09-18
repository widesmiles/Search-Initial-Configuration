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

main_folder = 'E:\model debug\SearchInitialConfiguration'

# node_num = 4283
max_loop_times = 1000
loop_time = 0

# read initial disp from step-1-0
subprocess.Popen('abaqus job={} int'.format('Step-1'),shell=True)
status_filename = 'Step-1'
status_code = 0
time.sleep(20)
while status_code == 0:
    time.sleep(5)
    status_code = check_sta(status_filename)
initial_step1_name = 'Step-1.dat'
print('The Step 1 procedure has been done !!!')
# with open(os.path.join(main_folder,initial_step1_name)) as initial_step1:
#     lines = initial_step1.readlines()
#     count = 0
#     for line in lines:
#         if 'THE FOLLOWING TABLE IS PRINTED FOR NODES BELONGING TO NODE SET ASSEMBLY_ALLNODES' in line:
#             node_output_linenum = count + 5
#         count = count + 1
#     for i in range(node_num):
#         temp_line = lines[node_output_linenum+i].split(' ')
#         dis_line = []
#         for j in range(len(temp_line)-1):
#             if len(temp_line[j]) > 0:
#                 if j == 0:
#                     dis_line.append(int(temp_line[j]))
#                 if j > 0:
#                     dis_line.append(float(temp_line[j]))
#         dis_list.append(dis_line)
#         dis_data = np.array(dis_list)

dis_data, node_num = dis_info(os.path.join(main_folder,initial_step1_name))
initial_NodesInfo = ObtainNodeInfo(os.path.join(main_folder,'Step-1.inp'))
initial_Nodes = np.array(initial_NodesInfo)
initial_X0 = EffectiveNodes(initial_Nodes, dis_data[:,0])
X0 = np.array(initial_X0)[:,1:]

relative_tol = 0.001
absolute_tol = 1e-5
implement_dis = np.zeros((node_num,4))
implement_dis[:,0] = dis_data[:,0]
implement_dis[:,1:] = -dis_data[:,1:]
last_dis = np.zeros((node_num,4))
last_dis[:,0] = dis_data[:,0]
last_dis[:,1:] = -dis_data[:,1:]
penalty = 1.00
        
while  loop_time<1 or disp_magnitude(Xn, X0).max()>absolute_tol:

    with open('Step3_loop.txt','w') as step3Loop:
        step3Loop.writelines(str(loop_time))
    step3Loop.close()
    
    disp_sub_name = 'adjust_disp_' + str(loop_time) + '.for'
    WriteNewDisp(disp_sub_name, implement_dis)
    step2_job_name = 'Step-2-' + str(loop_time)
    subprocess.Popen('abaqus job={} inp={} user={} int'.format(step2_job_name,'Step-2',disp_sub_name),shell=True)
    status_code = 0
    status_filename = 'Step-2-' + str(loop_time)
    time.sleep(20)
    while status_code == 0:
        time.sleep(5)
        status_code = check_sta(status_filename)
        # with open(status_filename,'r') as f:
            # status_code = int(f.read())
    print('The Step 2 at loop %d procedure has been done !!!'%loop_time)
    subprocess.Popen('abaqus cae nogui={}'.format('GenerateStep3_2.py'),shell=True)
    step3_code = 0
    status_filename = 'Step-3.txt'
    time.sleep(20)
    while status_code == 0:
        time.sleep(5)
        with open(status_filename,'r') as f:
            status_code = int(f.read())
    
    step3_inp_name = 'Step-3-' + str(loop_time) + '.inp'
    AddNodePrint(step3_inp_name)
    last_NodeInfo = ObtainNodeInfo(step3_inp_name)
    last_Nodes = np.array(last_NodeInfo)
    last_effective_Nodes = EffectiveNodes(last_Nodes, dis_data[:,0])
    subprocess.Popen('abaqus job={} int'.format(step3_inp_name[0:-4]),shell=True)
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
    Xn = last_effective_Nodes[:,1:] + dis_data[:,1:]
    implement_dis = np.zeros((node_num,4))
    implement_dis[:,0] = dis_data[:,0]
    # implement_dis[:,1:] = -(Xn - last_effective_Nodes[:,1:] - (Xn - X0))*penalty
    implement_dis[:,1:] = -(X0-(last_effective_Nodes[:,1:]-(Xn-X0)))*penalty
    loop_time = loop_time + 1
    print('The max error if displacement field is %8.10f. '%disp_magnitude(Xn, X0).max())