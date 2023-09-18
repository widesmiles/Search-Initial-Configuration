c      allocate a global module to save initial vector values at initial increment        
       MODULE GLOBAL
       IMPLICIT NONE
C         INTEGER,SAVE::ELENLOC=0
C         INTEGER,SAVE::TIPELE(1:1000)
       INTEGER,SAVE::COUNT=0
       INTEGER,SAVE::DSCOUNT(1:2)=-1
c      it may more suitable to allocate a static sequence       
       real*8,SAVE::TIPNODES(1:300000)=0.d0
c       real*8,ALLOCATABLE::TIPNODES(:)
       END MODULE GLOBAL
      SUBROUTINE DISP(U,KSTEP,KINC,TIME,NODE,NOEL,JDOF,COORDS)
      use global
C
      INCLUDE 'ABA_PARAM.INC'
C
      DIMENSION U(3),TIME(2),COORDS(3)
      double precision refnode(3)

C     
      refnode(1) = 2.5d0
      refnode(2) = 2.5d0
      refnode(3) = 2.5d0
      if (kinc.le.1) THEN
      if (jdof.eq.1) then
            TIPNODES(3*(node-1)+1) = COORDS(1)-refnode(1)
      elseif (jdof.eq.2) then
            TIPNODES(3*(node-1)+2) = COORDS(2)-refnode(2)
      else
            TIPNODES(3*node) = COORDS(3)-refnode(3)
      endif
      endif
      U(1) = 0.d0
      U(2) = 0.d0
      U(3) = 0.d0
      if(jdof.eq.3) then
      U(1) = 1.d0
      endif
      if (kinc.le.3) then
      print*,TIPNODES(3*(node-1)+1)
      print*,TIPNODES(3*(node-1)+2)
      print*,TIPNODES(3*node)
      endif


      RETURN
      END