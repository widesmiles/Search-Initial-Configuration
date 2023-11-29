# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 20:46:45 2022

@author: Asuka
"""

import os
import numpy as np
import pandas as pd
import math


def WriteNewDisp(subname, dislist):
    
    np.set_printoptions(suppress=True)
    Node = dislist[:,0]
    U1 = dislist[:,1]
    U2 = dislist[:,2]
    U3 = dislist[:,3]
    
    with open(subname,'w') as new_sub:
        new_str = ''
        new_str = new_str + '      SUBROUTINE DISP(U,KSTEP,KINC,TIME,NODE,NOEL,JDOF,COORDS)\n'
        new_str = new_str + "      INCLUDE 'ABA_PARAM.INC'\n"
        new_str = new_str + '      DIMENSION U(3),TIME(2),COORDS(3)\n'
        new_str = new_str + '      U(1) = 0.d0\n'
        new_str = new_str + '      U(2) = 0.d0\n'
        new_str = new_str + '      U(3) = 0.d0\n'
        new_str = new_str + '      select case (NODE)\n'
        for i in range(dislist.shape[0]):
            new_str = new_str + '      case (' + str(int(Node[i])) + ')\n'
            if U1[i]>=0:
                new_str = new_str + '      IF (JDOF.EQ.1) THEN\n'
                new_str = new_str + '      U(1) = TIME(1)*' + str('%8.10f' % U1[i]) + 'd0\n'
                new_str = new_str + '      ENDIF\n'
            else:
                new_str = new_str + '      IF (JDOF.EQ.1) THEN\n'
                new_str = new_str + '      U(1) = -TIME(1)*' + str('%8.10f' % abs(U1[i])) + 'd0\n'
                new_str = new_str + '      ENDIF\n'
            if U2[i]>=0:
                new_str = new_str + '      IF (JDOF.EQ.2) THEN\n'
                new_str = new_str + '      U(1) = TIME(1)*' + str('%8.10f' % U2[i]) + 'd0\n'
                new_str = new_str + '      ENDIF\n'
            else:
                new_str = new_str + '      IF (JDOF.EQ.2) THEN\n'
                new_str = new_str + '      U(1) = -TIME(1)*' + str('%8.10f' % abs(U2[i])) + 'd0\n'
                new_str = new_str + '      ENDIF\n'
            if U3[i]>=0:
                new_str = new_str + '      IF (JDOF.EQ.3) THEN\n'
                new_str = new_str + '      U(1) = TIME(1)*' + str('%8.10f' % U3[i]) + 'd0\n'
                new_str = new_str + '      ENDIF\n'
            else:
                new_str = new_str + '      IF (JDOF.EQ.3) THEN\n'
                new_str = new_str + '      U(1) = -TIME(1)*' + str('%8.10f' % abs(U3[i])) + 'd0\n'
                new_str = new_str + '      ENDIF\n'
        new_str = new_str + '      end select\n'
        new_str = new_str + '      return\n'
        new_str = new_str + '      end'
        new_sub.writelines(new_str)
    new_sub.close()
    
def disp_magnitude(X1,X2):
    X_m = np.zeros((X1.shape[0],1))
    for i in range(X1.shape[0]):
        X_m[i] = math.sqrt((X1[i,0]-X2[i,0])**2.0+(X1[i,1]-X2[i,1])**2.0+(X1[i,2]-X2[i,2])**2)
    return X_m

def dis_info(dat_name):
    dis_list = []
    with open(dat_name) as initial_step1:
        lines = initial_step1.readlines()
        count = 0
        for line in lines:
            if '   THE FOLLOWING TABLE IS PRINTED FOR NODES BELONGING TO NODE SET ASSEMBLY_ALLNODES' in line:
                node_output_start_line = count + 5
            if '   THE FOLLOWING TABLE IS PRINTED FOR NODES BELONGING TO NODE SET ASSEMBLY_FC' in line:
                node_output_end_line = count - 9
            count = count + 1
        node_num = node_output_end_line - node_output_start_line
        for i in range(node_num):
            temp_line = lines[node_output_start_line+i].split()
            dis_line = []
            for j in range(len(temp_line)):
                if j == 0:
                    dis_line.append(int(temp_line[j]))
                if j > 0:
                    dis_line.append(float(temp_line[j]))
            dis_list.append(dis_line)
            dis_data = np.array(dis_list)
    return dis_data, node_num

def check_sta(strname):
    fname = strname +'.sta'
    if(os.path.exists(fname) == True):
        with open(fname,'r') as f:
            lines = f.readlines()
            last_line = lines[-1]
        if last_line ==  ' THE ANALYSIS HAS COMPLETED SUCCESSFULLY\n':
            status = 1
        else:
            print(strname+' has not been completed ... ...')
            status = 0
    else:
        status = 0
    return status

def ChangeConfiguration(initial_inp_name,current_inp_name,loop_time):
    with open(initial_inp_name,'w') as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            if '*Assembly, name=Assembly' in line:
                configuration_line_num = count + 2
            count = count + 1
        new_lines = lines
        configuration_line = lines[configuration_line_num]
        words = configuration_line.split(',')
        word1 = words[0]
        word2 = ' library=' + 'Step-2-' + str(loop_time)
        word3 = words[2]
        new_configuration_line = word1 + word2 + word3
        new_lines[configuration_line_num] = new_configuration_line
    f.close()
    with open(current_inp_name,'w') as nf:
        nf.writelines(new_lines)
    nf.close()

def AddNodePrint(inpname):
    new_str = ''
    with open(inpname,'r') as f1:
        lines = f1.readlines()
        count = 0
        for line in lines:
            if '*End Step' in line:
                endline = count
            else:
                new_str = new_str + line
            count = count + 1
    f1.close()
    new_str = new_str + '*node print, nset=allnodes\n'
    new_str = new_str + 'U\n'
    new_str = new_str + '*node print, nset=FC\n'
    new_str = new_str + 'PCAV\n'
    new_str = new_str + '*End Step\n'
    with open(inpname,'w') as f2:
        f2.writelines(new_str)
    f2.close()
    
def ObtainNodeInfo(initial_inp_filename):
    Node_info = []
    with open(initial_inp_filename) as initial_inp:
        lines = initial_inp.readlines()
        count = 0
        start_count = 1
        end_count = 1
        for line in lines:
            if '*Part, name=Part-1' in line and start_count==1 :
                node_start_line = count + 2
                start_count = 0
            if '*Element' in line and end_count==1:
                node_end_line = count
                end_count = 0
            count = count + 1
        part_node_num = node_end_line - node_start_line
        for line in lines[node_start_line:node_end_line]:
            words = line.split(',')
            Node_info.append([int(words[0]),float(words[1]),float(words[2]),float(words[3])])
    initial_inp.close()
    return Node_info

def EffectiveNodes(all_Node_info,target_nodeset):
    effective_nodes_info = np.zeros((len(target_nodeset),4))
    count = 0
    for node_info in all_Node_info:
        if node_info[0] in target_nodeset:
            effective_nodes_info[count,:] = node_info
            count = count + 1
    return effective_nodes_info

def FC_info(dat_name):
    with open(dat_name,'r') as datfile:
        lines = datfile.readlines()
    for i,line in enumerate(lines):
        if '          THE ANALYSIS HAS BEEN COMPLETED' in line:
            P_line = lines[i-9]
            break
    P_end = float(P_line.split()[-1])
    return P_end
            

# def JudgeIncNum(sta_filename):
#     with open(sta_filename) as f:
#         lines = f.realines()
#         for line in lines:
#             if 'THE ANALYSIS HAS COMPLETED SUCCESSFULLY' in line:
