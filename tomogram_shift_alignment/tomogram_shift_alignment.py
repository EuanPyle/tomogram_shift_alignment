from pathlib import Path
from thefuzz import process

import os,sys
import starfile
import typer

#For each tomogram pairing
#----- ONE SCRIPT -----
#Read tomogram size, automatically set patch size, numbers, and boudnaries

#Generate command, and run os.system(COMMAND)
#end

#----- ANOTHER SCRIPT -----
#Read IMOD output

#Parse into array

#For CC values of over 0.95 (optimise), take X Y and Z shifts, if none or few, bail and warn

#Average shifts, warn if SD too high

#Unbin the shifts

#Save shifts in .txt file in  a folder
#end

#end for loop

#----- ANOTHER SCRIPT -----
#read .txt files

#open star file and apply shifts relative to each tomogram and re-write



#============================================================================================================================

cli = typer.Typer()

@cli.command()
def tomogram_shift_alignment(
    original_tomograms_dir: Path,
    new_tomograms_dir: Path,
    particles_star: Path,
    tomogram_binning: float,
) -> Path: ##### CORRECT? Output should be path to new file
    """tomogram_shift_alignment
    
    Requirements 
    ---------------
    Your tomogram names must match rlnTomoName in the particles star file and must use either the .mrc or .st extensions
    
    Parameters
    ---------------
    
    original_tomograms_dir : path to the directory containing the tomograms from which subtomogram averaging has already been done \n
    new_tomograms_dir : path to the directory containing the tomograms which have been generated using a 'new' tilt series alignment methods 
        and are therefore shifted compared to the original tomograms \n
    particles_star : path to the star file containing subtomogram particle positions for the tomograms in original_tomograms_dir \n
    tomograms_binning : binning level (IMOD convention) of your tomograms so particle shifts can be written in unbinned coordinates for 
        RELION 4.0 \n 
    
    Returns
    ---------------
    
    adjusted_star_file : a star file with adjusted subtomogram coordinates which should match the tomograms in new_tomograms_dir \n
    
    Example Input
    ---------------
    
    tomogram_shift_alignment './' '../new_tomos/' './particles.star' 8
    """
    
    #Test IMOD is loaded
    imod_test = os.popen('dm2mrc').read()
    if imod_test == '':
        print('Can\'t find dm2mrc, try loading imod outside of this script first. Birkbeck users type: module load imod')
        sys.exit()
    
    original_tomo_list = list(Path(original_tomograms_dir).glob('*'))
    for idx in range(len(original_tomo_list)):
        original_tomo_list[idx] = original_tomo_list[idx].name
    
    new_tomo_list = list(Path(new_tomograms_dir).glob('*'))
    for idx in range(len(new_tomo_list)):
        new_tomo_list[idx] = new_tomo_list[idx].name
    
    #Match tomograms from original to new
    matched_new_tomograms = {}
    for tomo in original_tomo_list:
        matched_new_tomograms.update({tomo:process.extractOne(tomo,new_tomo_list)[0]})    
    
NEWSCRIPT: READ MRC FIZE, automatically set patch size, numbers, and boudnaries, generate command  
    
    for tomo in matched_new_tomograms:
        run_corrsearch3d((Path(original_tomograms_dir) / tomo),(Path(new_tomograms_dir) / matched_new_tomograms[tomo]))
    
    print('Working')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


