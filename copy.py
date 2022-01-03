# 20/12/2021
#
# SP - Dummy script to create and copy files in directories.

import numpy as np
import os

elements = ['Ag',
'Al',
'Ar',
'As',
'At',
'Au',
'Ba',
'Be',
'B',
'Bi',
'Br',
'Ca',
'Cd',
'Ce',
'C',
'Cl',
'Co',
'Cr',
'Cs',
'Cu',
'Dy',
'Er',
'Eu',
'Fe',
'F',
'Ga',
'Gd',
'Ge',
'He',
'Hf',
'H',
'Hg',
'Ho',
'I',
'In',
'Ir',
'K',
'Kr',
'La',
'Li',
'Lu',
'Mg',
'Mn',
'Mo',
'Na',
'Nb',
'Nd',
'Ne',
'N',
'Ni',
'O',
'Os',
'Pb',
'Pd',
'P',
'Pm',
'Po',
'Pr',
'Pt',
'Rb',
'Re',
'Rh',
'Rn',
'Ru',
'Sb',
'Sc',
'Se',
'S',
'Si',
'Sm',
'Sn',
'Sr',
'Ta',
'Tb',
'Tc',
'Te',
'Ti',
'Tl',
'Tm',
'V',
'W',
'Xe',
'Yb',
'Y',
'Zn',
'Zr']

#for ii in np.arange(100):
#  os.system('mkdir '+str(elements[ii]))
#  os.system('mv '+str(elements[ii])+'.*  '+str(elements[ii])+'/')
#  os.system('mv '+str(elements[ii])+'.*  '+str(elements[ii])+'/')

# for ii in np.arange(100):
#   os.system('cd '+str(elements[ii])+'/ && git mv '+str(elements[ii])+'.GGA_PBE-JTH.xml '+str(elements[ii])+'_std.xml && cd ../')

for ii in np.arange(100):
  exec_str = 'cd '+str(elements[ii])+'/ && cp '+str(elements[ii])+'_std.upf '+str(elements[ii])+'_str.upf && cd ../'
  # print(exec_str)
  os.system(exec_str)
  
  exec_str = 'cd '+str(elements[ii])+'/ && cp '+str(elements[ii])+'_std.xml '+str(elements[ii])+'_str.xml && cd ../'
  os.system(exec_str)

# cp ../jth-lda-upf/PBE-sp-UPF/As.LDA-PW-paw.UPF As/As_str.upf 
# cp ../jth-lda-upf/PBE-sp-UPF/Bi.LDA-PW-paw.UPF Bi/Bi_str.upf 
# cp ../jth-lda-upf/PBE-sp-UPF/In.LDA-PW-paw.UPF In/In_str.upf 
# cp ../jth-lda-upf/PBE-sp-UPF/Pb.LDA-PW-paw.UPF Pb/Pb_str.upf 
# cp ../jth-lda-upf/PBE-sp-UPF/Sb.LDA-PW-paw.UPF Sb/Sb_str.upf 
# cp ../jth-lda-upf/PBE-sp-UPF/Sn.LDA-PW-paw.UPF Sn/Sn_str.upf 
# cp ../jth-lda-upf/PBE-sp-UPF/Tl.LDA-PW-paw.UPF Tl/Tl_str.upf

# for ii in np.arange(100):
#   exec_str = 'cd '+str(elements[ii])+'/ && cp ../../paw_pw_stringent/'+str(elements[ii])+'.xml '+str(elements[ii])+'_str.xml && cd ../'
#   # print(exec_str)
#   os.system(exec_str)
