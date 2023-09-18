# How to prepare all necessary files and implement the modification procedure.

Bio-tissue is often in a certain state of pre-stress in the human body, for example, the cornea is under intraocular pressure, the blood vessel is under blood pressure and et al. So whatever method we use to measure the configuration of the tissue, we can not get the load-free configuration(or be called initial configuration), which is needed in abaqus modeling.

In this project, we use the direct method to obtain the initial configuration. Assume that we have a target configuration $A$ and a known load $F$. Then we start a simple iterative process:
1. start with our only known target configuration $A$ as initial configuration $A_0$
2.  apply load $F$ to $A_0$, and get the result configuration $A^*$
3.  calculate the difference between $A^*$ and the target configuraiton $A$, to get the difference field $U=A^* -A$
4.  Check if the difference field $U$ is small enough, if yes, then stop the iteration and $A_0$ is the result of  initial configuration; if not, then update the initial configuration $A_0$ by $A_0 = A_0 - U$ and go back to step 2.

In this project, we use a internal pressure loaded cylinder as an example of the direct method. You can simply replace the example job file to your own one, the code still works. You should refer to different folders regarding to the dimension of your model, 2D or 3D.

## Prepare the input files

- First, after you have complete your own abaqus job file, you need to select all the nodes that are not fixed(all nodes in the model except the nodes of the fixed boundary) and create a nodeset named `allnodes`.
- Then you can write the `.inp` file of your job, and save it as `Step-1.inp` in your abaqus working directory.
- You need to add the following code to the end of your `.inp` file before the line of `*End Step`:
    ```
    *node print, nset=allnodes
    U
    ```


## Changes to be made when you use your own job file

- In the code file `IdentifyInitialConfiguration.py`, you need to change the `*Part, name=cylinder` in line 157 to your own part name.
- the code is for 3D models, if yours is 2D, you need to make the following changes:
  - d

## Problems

- `IdentifyInitialConfiguration.py` line 84, why `len(temp_line)` need to -1?
- 