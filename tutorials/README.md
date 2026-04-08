# Python tutorials for using the PROMICE Sentinel-1 ice velocity dataset

Jupyter Notebook tutorials can be found here to provide an introduction to fetching and handling the 
PROMICE Sentinel-1 ice velocity dataset.

## Getting started

To ensure that you have a Python environment configured, we have provided a conda environment file that 
contains all of the dependencies needed to run the tutorials. A conda environment can be created from this 
file like so:

```bash
conda env create -f environment.yml
```

## Tutorial contents
Each tutorial contains several essential routines using the [xarray](https://xarray.dev/) Python package. We have chosen different 
locations to showcase these routines - Sermeq Kujalleq, Narsap Sermia, Helheim Glacier and Hagen Bræ.

The main thing that differentiates the tutorials is that they each contain different approaches to 
downloading the PROMICE ice velocity dataset. The Sermeq Kujalleq and Narsap Sermia tutorials walk through 
downloading through the [GEUS Dataverse](https://dataverse.geus.dk/dataverse/Ice_velocity/), whilst the 
Helheim Glacier and Hagen Bræ tutorials outline how to fetch data from the [GEUS Thredds server](https://thredds.geus.dk/) 
using OpenDAP querying.

For beginners with no experience using xarray, we recommend starting with the Sermeq Kujalleq tutorial as 
this outlines how to handle xarray Dataset objects.

### [Sermeq Kujalleq](https://github.com/GEUS-Glaciology-and-Climate/Sentinel-1_Greenland_Ice_Velocity/blob/main/tutorials/promice_iv_sermeq_kujalleq_tutorial.ipynb)
1. Download a NetCDF file from the dataset hosted on the Dataverse portal
2. Visualise velocities over a defined region
3. Return the dataset values at a given point
4. Produce a velocity profile across a flowline

### [Narsap Sermia](https://github.com/GEUS-Glaciology-and-Climate/Sentinel-1_Greenland_Ice_Velocity/blob/main/tutorials/promice_iv_narsap_sermia_tutorial.ipynb)
1. Download a series of dataset files from the Dataverse portal
2. Compute average velocities over a given region
3. Produce a time-series of velocities at a given point
4. Produce a time-series of average velocities across a flowline

### [Helheim Glacier](https://github.com/GEUS-Glaciology-and-Climate/Sentinel-1_Greenland_Ice_Velocity/blob/main/tutorials/promice_iv_helheim_glacier_tutorial.ipynb)
1. Connecting to the PROMICE Ice Velocity aggregated dataset using OpenDAP
2. Querying and fetching data from a given point
3. Querying and fetching data from a given region

### [Hagen Bræ](https://github.com/GEUS-Glaciology-and-Climate/Sentinel-1_Greenland_Ice_Velocity/blob/main/tutorials/promice_iv_hagen_brae_tutorial.ipynb)
1. Connecting to the PROMICE Ice Velocity dataset file series using OpenDAP
2. Constructing and computing a velocity time-series from a flowline


## Any questions?

If you would like to raise an issue or request a new feature/tutorial then please post an issue 
[here](https://github.com/GEUS-Glaciology-and-Climate/Sentinel-1_Greenland_Ice_Velocity/issues) and use the 
word "tutorial" in the issue title.
