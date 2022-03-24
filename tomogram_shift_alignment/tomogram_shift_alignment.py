import os, starfile

#Set up git

#Set up pip folder structure (modern)

#Requirements: your tomogram names match rlnTomoName in star file with either .mrc or .st ends

#Click inputs, location of original tomograms, location of shifted tomograms, particle star file, tomogram binning level

#Check IMOD is loaded

#Generate list of tomograms

#Find corresponding tomograms (fuzzy match)

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
