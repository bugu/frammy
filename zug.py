import subprocess, os, sys

def process():
    print("Control Source !!")
    print ("Press enter for default time")
    time = input("Time: ")
    #print time
    if time == "":
        time = "00:00:14"
    else:
        return
    tt = os.getcwd()

    cwd = ("%s/Source"%(os.getcwd()))

 
    # get a list of files that have the extension mp4
    filelist = filter(
        lambda f: f.split('.')[-1] == 'mp4', 
        os.listdir(cwd)
    )
 
    # get frame from each
    for file in filelist:
        frame(file,time)

def frame(file,time):
    cut = ''.join(file.split('.')[:-1])
    jpeg = '{}.jpg'.format(cut)
    cwd = os.getcwd()
    subprocess.call('./ffmpeg -ss %s -i %s/Source/%s -frames:v 1 %s/Out/%s'%(time,cwd,file,cwd,jpeg),shell=True)
	



process()
