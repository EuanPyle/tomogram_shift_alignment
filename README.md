## tomogram_shift_alignment

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/dynamo2m.svg)](https://pypi.python.org/pypi/dynamo2m/)

#### Outline
Different tomogram generation and/or reconstruction techniques often generate tomograms with slightly different coordinates. This makes comparing the attainable resolution of the structure from these tomograms difficult. This program compares the shifts between two of the same tomogram which were constructed by different methods, and adjusts the particle coordinates of a star file to fit the new tomogram.

This is designed for RELION v4.0 star files. The generated star file should be imported into RELION 4.0 using Import Coordinates. 

#### Installation and Usage
#### Requirements
- Python (3.0 or later)

Installation is carried out via:
```sh
pip install tomogram_shift_alignment
```

Invoke from the command line via typing:
```sh
tomogram_shift alignment [original_tomograms] [new_tomograms] [particles_star] [tomogram_binning] [Optional: tomogram_trimming]

e.g.

tomogram_shift alignment './tomograms' './new_tomograms' './run_data.star' 8 60
```

Where original_tomograms is the path to directory containing original tomograms where particles were picked. New tomograms is the path to directory containing new tomograms where the coordinates don't match. particles_star is a star file containing refinemed particle positions and angles. Tomogram binning is the binning level of the tomograms. An optional input is tomogram_trimming which is the number (in percent) to trim the tomograms by from the outer edges. This is to avoid comparison of the tomograms in empty space. Default is 40%. Use a higher value if your sample is perfectly centred in the tomogram and vice versa. 
