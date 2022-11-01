import shutil
import time, glob

outfilename = 'mols.sdf'

with open('mols.sdf', 'wb') as outfile:
    for filename in glob.glob('*.sdf'):
        if filename == outfilename:
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)
