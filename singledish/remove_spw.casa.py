import os
import glob

processingDir = '/home/heh15/research/Antennae_GMCs/singledish/antennae/processing_singledish_antennae/'
rawDir = processingDir + 'raw/'
calDir = processingDir + 'calibration/'

rawFiles = glob.glob(rawDir+'*.asdm.sdm/')
rawFiles_temp = [f.replace('raw/', 'calibration/') for f in rawFiles]
msFiles = [f.replace('.asdm.sdm', '.ms') for f in rawFiles_temp]

for infile in msFiles:
    outfile = infile.replace('.ms', '_spwFlag.ms')
    split(vis=infile, outputvis=outfile, datacolumn='DATA', spw='0~20,23,24')
    rmtables(infile)
    os.rename(outfile, infile)

# split(vis='test/uid___A002_Xf3bcf1_X444a.ms', outputvis='test/uid___A002_Xf3bcf1_X444a.ms', spws='0~20,23,24')

