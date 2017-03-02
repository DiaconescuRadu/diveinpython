#!/usr/bin/env python3
import os
import shutil

def copy_contents(folderName):
    for file in os.listdir(folderName):
        if (file.endswith(".NEF")):
            nef_file = os.path.join(input_folder, folderName, file)
            print(nef_file + " -> " + nef_folder)
            shutil.copy(nef_file, nef_folder)
        if (file.endswith(".JPG")):
            jpg_file = os.path.join(input_folder, folderName, file)
            print(jpg_file + " -> " + folder_name)
            shutil.copy(jpg_file, folder_name)
        if (file.endswith(".jpg")):
            jpg_file = os.path.join(input_folder, folderName, file)
            print(jpg_file + " -> " + folder_name)
            shutil.copy(jpg_file, folder_name)
        if (file.endswith(".dng")):
            jpg_file = os.path.join(input_folder, folderName, file)
            print(jpg_file + " -> " + dng_folder)
            shutil.copy(jpg_file, folder_name)
        if (file.endswith(".MOV")):
            mov_file = os.path.join(input_folder, folderName, file)
            print(mov_file + " -> " + folder_name)
            shutil.copy(mov_file, folder_name)   
        if (file.endswith(".mp4")):
            mov_file = os.path.join(input_folder, folderName, file)
            print(mov_file + " -> " + folder_name)
            shutil.copy(mov_file, folder_name)   

folder_name = input("Name of the picture directory: ")
picasa_folder = os.path.join(folder_name, folder_name + " - picasa");
facebook_folder = os.path.join(folder_name, folder_name + " - facebook");
nef_folder = os.path.join(folder_name, "nef");
dng_folder = os.path.join(folder_name, "dng");

if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    os.makedirs(picasa_folder)
    os.makedirs(facebook_folder)
    os.makedirs(nef_folder)

#print possible sources to copy from

phoneRootLocation = "/run/user/1000/gvfs/"
nikonRootLocation = "/media/griz"

if len(os.listdir(phoneRootLocation)):
    inputRootLocation = phoneRootLocation
    photosSubfolder = "Internal storage/DCIM/Camera"
else:
    inputRootLocation = nikonRootLocation
    photosSubfolder = "DCIM"

count = 0
for file in os.listdir(inputRootLocation):
    count = count + 1
    print(str(count) + ". " + file)

source_index = input("Choose source: ")

count = 0
for file in os.listdir(inputRootLocation):
    count = count + 1
    if (str(count) == source_index):
        input_folder = os.path.join(inputRootLocation, file, photosSubfolder)

print("Input folder is: " + input_folder)

if (inputRootLocation == nikonRootLocation):
    for subdir in os.listdir(input_folder):
        print("Copying files from subdirectory " + input_folder)
        copy_contents(os.path.join(input_folder, subdir))
else:
    copy_contents(input_folder)
