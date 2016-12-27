'''
Created on 27 dec. 2016

@author: radi961
'''
import os
import glob

def list_comprehension(initialList):
    return [elem * 2 for elem in initialList]

if __name__ == "__main__":
    print("Running the main loop")
    print(os.getcwd())
    currentDir = os.getcwd()
    (parentDir, dir) = os.path.split(currentDir)
    os.chdir(os.path.expanduser('~'))
    print(os.getcwd())
    
    #for item in os.listdir('.'):
    #    print(item)
    
    print(glob.glob('*.log'))
    
    print(list_comprehension([1, 2]))
    
    #list filtering
    print("List filtering")
    initialList = [1, 2, 3, 4]
    
    print([item * 2 for item in initialList if item > 3])
    
    #dictionary comprehension
    print("Dictionary comprehension")
    
    folderList = [f for f in os.listdir('.')]
    
    print(folderList)
    
    folderStatDict = { f : os.stat(f) for f in folderList}
    
    print(folderStatDict['VirtualBox VMs'])
    
    testDict = {1 : 'a', 2 : 'b', 3 : 'c'}
    
    reversedDict = {value : key for (key, value) in testDict.items()}
    
    print(reversedDict)
