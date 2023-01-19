from spectral_cube import SpectralCube
from astropy import units as u

###########################################################
# directories

Dir = '/home/heh15/research/Antennae_GMC/'
scriptDir = Dir + 'script/'
imageDir = Dir + 'images/'

###########################################################
# basic settings

lines = ['12CO10','12CO21','13CO21']
filenames = ['ngc_4038_4039_12m_ext+12m_com+7m+tp_co10_pbcorr_round_k.fits',
            'ngc_4038_4039_12m_ext+12m_com+7m+tp_co21_pbcorr_round_k.fits',
            'ngc_4038_4039_12m_ext+12m_com+7m+tp_13co21_pbcorr_round_k.fits']

###########################################################
# main program


for i, filename in enumerate(filenames):
    kcube = SpectralCube.read(imageDir+filename)
    kcube.allow_huge_operations=True
    cube = kcube.to(u.Jy/u.beam)
    cube.write(imageDir+'Antennae_'+lines[i]+'_pbcorr_round_Jy.fits',overwrite=True)
