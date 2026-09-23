import os
import shutil

# Creation des dossiers
os.mkdir("Test 2") # valeur donné par l'utilisateur
os.makedirs("Test 2/riivolution")
os.makedirs("Test 2/riivolution/config")
os.makedirs("Test 2/contents")
os.makedirs("Test 2/contents/TUTO") # si le mod en a besoin
os.makedirs("Test 2/contents/sound") # si le mod en a besoin
os.makedirs("Test 2/contents/HomeButton2") # si le mod en a besoin

# Copier les fichiers important comme les fichiers .xml de riivolution par exemple
shutil.copy('mods/riivolution files/Rayman Raving Rabbids.xml', 'Test 2/riivolution/')
shutil.copy('mods/riivolution files/RRR1.xml', 'Test 2/riivolution/')
shutil.copytree('.gitignore/Rayman Raving Rabbids 1/DATA/files', 'Test 2/contents/')


            
