from pathlib import Path

import os,sys
import mrcfile

def run_corrsearch3d(
    path_to_original: Path,
    path_to_new: Path,
    tomogram_trimming: float
):
    """Reads mrc files size, sets patch size, numbers, boundaries, and runs IMODs corrsearch3d function
    """
    
    #Read mrc files
    mrc_original = mrcfile.open(path_to_original)
    mrc_new = mrcfile.open(path_to_new)
    
    #Extract dimensions
    ori_shape = mrc_original.data.shape
    new_shape = mrc_new.data.shape
    
    #If dimensions don't match, bail
    if ori_shape != new_shape:
        print(f"The dimensions of matched original tomogram {path_to_original.name} and new tomogram {path_to_new} do not match. Bailing...")
        sys.exit()
    
    #Set XYZ dimensions
    x_dim = ori_shape[2]
    y_dim = ori_shape[1]
    z_dim = ori_shape[0]
    
    #Set XYZ min and max by applying trimming
    actual_trim = (tomogram_trimming / 2) / 100
    x_min = 0 + (x_dim * actual_trim)
    x_max = x_dim - ((x_dim * actual_trim))
    y_min = 0 + (y_dim * actual_trim)
    y_max = y_dim - ((y_dim * actual_trim))
    z_min = 0 + (z_dim * actual_trim)
    z_max = z_dim - ((z_dim * actual_trim))
        
    #Other parameters, set for the user automatically
    
    largest_dimension = {'x_dim': x_dim,'y_dim': y_dim,'z_dim':z_dim}
    result = (max(largest_dimension,key=largest_dimension.get))
    largest_dimension = largest_dimension[result]
    
    patch_size = largest_dimension / 10 
    
    max_shift = largest_dimension / 5
    
    number_patches = 5
    
    #Run command
    os.system(f"corrsearch3d -ref {str(path_to_original)} -align {str(path_to_new)} -maxshift {int(max_shift)} -size {int(patch_size)},{int(patch_size)},{int(patch_size)} -number {int(number_patches)},{int(number_patches)},{int(number_patches)} -xminmax {int(x_min)},{int(x_max)} -yminmax {int(y_min)},{int(y_max)} -zminmax {int(z_min)},{int(z_max)} -output {path_to_original.stem}.txt")
  
