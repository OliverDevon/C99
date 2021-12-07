import os, shutil
path = input('Enter the name of the directory please: ')
listOfFiles = os.listdir(path)
print(listOfFiles)
for file in listOfFiles:
    name,Ext=os.path.splitext(file)
    Ext = Ext[1:]
    if Ext =='':
        continue
    if os.path.exists(path+'/'+Ext):
        shutil.move(path+'/'+file,path+'/'+Ext+'/'+file)
    else:
        os.mkdir(path+'/'+Ext)
        shutil.move(path+'/'+file,path+'/'+Ext+'/'+file)