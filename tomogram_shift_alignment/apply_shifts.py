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
        
    #Delete rows with CC lower than 0.6
    delete_list = []
    for idx in range(len(imod_output)):
        if imod_output[idx][6] < 0.6: 
            delete_list.append(idx) 
        
    #Warn no rows
    if len(delete_list) == imod_output.shape[0]: 
        print(f"Warning, {full_tomo_name} has poor CC values (<0.6) between new and old tomogram and therefore the shifts are unreliable, averaging with the highest 6 CC values")
        imod_output = imod_output[imod_output[:,6].argsort()]
        imod_output = imod_output[-6:,:]
    else:
        imod_output = np.delete(imod_output,delete_list,axis=0)    
    
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
    if 'particles' in star:
        particles = star['particles']
    else:
        particles = star
    
    #Find rows of the tomogram of interest	
    idx = particles.index[particles['rlnTomoName'] == tomo_name.stem].tolist()
    
    for i in idx:
        particles.loc[particles.index[i],['rlnCoordinateX']] = particles.loc[i,'rlnCoordinateX'] + unbin_x
        particles.loc[particles.index[i],['rlnCoordinateY']] = particles.loc[i,'rlnCoordinateY'] + unbin_y
        particles.loc[particles.index[i],['rlnCoordinateZ']] = particles.loc[i,'rlnCoordinateZ'] + unbin_z
            
    starfile.write(particles,'tomogram_coordinates_shifted.star',overwrite=True)
    
    os.rename(f"./{full_tomo_name}", f"./tomogram_shifts/{full_tomo_name}")
    
	
    
