import os 

filenames = []

for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        filenames.append(os.path.join(subdir,file))

for file in filenames:
    if 'Depth' in file:
        print(file)
    # folder = os.getcwd()+mainfolder
    # print(folder)
    # for field in ['p','U']:
        # file   = folder+'/'+field
        # with open(file,'r') as f:
            # text = f.readlines()
            # text = text[22:43772]
