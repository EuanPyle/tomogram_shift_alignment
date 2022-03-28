from pathlib import Path

import os,sys
import starfile
import numpy as np

def apply_shifts(
    tomo_name: Path,
    particles_star: Path,
    tomogram_binning: float
):
    """Reads tomogram CC alignment output, applies shifts to star file"""
    
    #Define IMOD output
    full_tomo_name = f"{tomo_name.stem}.txt"
    
    #Read IMOD output into array
    imod_output = np.loadtxt(full_tomo_name, skiprows=1)
        
    #Delete rows with CC lower than 0.95
    delete_list = []
    for idx in range(len(imod_output)):
        if imod_output[idx][6] < 0.95: 
            delete_list.append(idx) 
    
    imod_output = np.delete(imod_output,delete_list,axis=0)
    
    #Warn no rows
    if imod_output.size == 0:
        print(f"Warning, {full_tomo_name.stem} has poor CC values (<0.95) between new and old tomogram and therefore the shifts are unreliable, bailing")
        return
    
    #Extract XYZ Coordinates
    imod_output = imod_output[:,3:6]
    
    #Mean of XYZ Coordinate shifts
    mean_x = np.mean(imod_output[:,0])
    mean_y = np.mean(imod_output[:,1])
    mean_z = np.mean(imod_output[:,2])
        
    #Unbin the shifts
    unbin_x = mean_x * tomogram_binning
    unbin_y = mean_y * tomogram_binning
    unbin_z = mean_z * tomogram_binning
        
    #Open star file and apply shifts relative to each tomogram and re-write
    star = starfile.read(particles_star)
    
    #Extract the particles from star file
    if len(star) > 1:
        particles = star['particles']
    else:
        particles = star
    
    #Find rows of the tomogram of interest	
    idx = particles.index[particles['rlnTomoName'] == tomo_name.stem].tolist()
    
    
    for i in idx:
        particles.loc[i,'rlnCoordinateX'] = particles.loc[i,'rlnCoordinateX'] + unbin_x
        particles.loc[i,'rlnCoordinateY'] = particles.loc[i,'rlnCoordinateY'] + unbin_y
        particles.loc[i,'rlnCoordinateZ'] = particles.loc[i,'rlnCoordinateZ'] + unbin_z

    if len(star) > 1:
        star['particles'] = particles
        starfile.write(star,'tomogram_shifted.star',overwrite=True)
    
    else:
        starfile.write(particles,'tomogram_shifted.star',overwrite=True)
