# Python tutorials for using the PROMICE Sentinel-1 ice velocity dataset

Jupyter Notebook tutorials can be found here to provide an introduction to fetching and handling the 
PROMICE Sentinel-1 ice velocity (PROMICE IV) dataset.

## Getting started

To ensure that you have a Python environment configured, we have provided a conda environment file that 
contains all of the dependencies needed to run the tutorials. A conda environment can be created from this 
file like so:

```bash
conda env create -f environment.yml
```

## Tutorial contents
Each tutorial contains several essential routines when fetching and handling the PROMICE IV dataset. 
[xarray](https://xarray.dev/) is the main Python package used to do this. We have chosen different 
locations to showcase these routines - Sermeq Kujalleq, Narsap Sermia, Helheim Glacier and Hagen Bræ.

The main thing that differentiates the tutorials is that they each contain different approaches to 
downloading the PROMICE IV dataset. The Sermeq Kujalleq and Narsap Sermia tutorials walk through 
downloading through the [GEUS Dataverse](https://dataverse.geus.dk/dataverse/Ice_velocity/), whilst the 
Helheim Glacier and Hagen Bræ tutorials outline how to fetch data from the [GEUS Thredds server](https://thredds.geus.dk/) 
using OpenDAP querying.

For beginners with no experience using xarray, we recommend starting with the Sermeq Kujalleq tutorial as 
this outlines an introduction to handling xarray Dataset objects.

### [Sermeq Kujalleq](https://github.com/GEUS-Glaciology-and-Climate/Sentinel-1_Greenland_Ice_Velocity/blob/main/tutorials/promice_iv_sermeq_kujalleq_tutorial.ipynb)
1. Download a PROMICE IV NetCDF file from the dataset hosted on the Dataverse portal
2. Visualise velocities over a defined region
3. Return the dataset values at a given point
4. Produce a velocity profile across a flowline

### [Narsap Sermia](https://github.com/GEUS-Glaciology-and-Climate/Sentinel-1_Greenland_Ice_Velocity/blob/main/tutorials/promice_iv_narsap_sermia_tutorial.ipynb)
1. Download a series of PROMICE IV files from the Dataverse portal
2. Compute average velocities over a given region
3. Produce a time-series of velocities at a given point
4. Produce a time-series of average velocities across a flowline

### [Helheim Glacier](https://github.com/GEUS-Glaciology-and-Climate/Sentinel-1_Greenland_Ice_Velocity/blob/main/tutorials/promice_iv_helheim_glacier_tutorial.ipynb)
1. Connect to the PROMICE IV aggregated file using OpenDAP
2. Query and fetch data from a given point
3. Query and fetch data from a given region

### [Hagen Bræ](https://github.com/GEUS-Glaciology-and-Climate/Sentinel-1_Greenland_Ice_Velocity/blob/main/tutorials/promice_iv_hagen_brae_tutorial.ipynb)
1. Connect to the PROMICE IV file series using OpenDAP
2. Construct and compute a velocity time-series from a flowline

### A note on OpenDAP querying with the GEUS Thredds server
OpenDAP querying with our Thredds server can be slow at times. This can be due to a multitude of things, including 
internet speed. If you are experiencing problems with fetching data through OpenDAP querying from the GEUS Thredds server 
then please consider reducing your query (either defining a smaller region or a narrower time range). 

Generally, the PROMICE IV aggregated file is slowest to work with (outlined in the Helheim Glacier tutorial), so please also 
consider working with the PROMICE IV file series on the Thredds server (as outlined in the Hagen Bræ tutorial).

If you are really struggling then it is best to resort to downloading files and using them locally. This can be 
achieved through the GEUS Dataverse (as outlined in the Sermeq Kujalleq and Narsap Sermia tutorials). Also, files can 
be downloaded manually through the GEUS Thredds server. 

## Any questions?

If you would like to raise an issue or request a new feature/tutorial then please post an issue 
[here](https://github.com/GEUS-Glaciology-and-Climate/Sentinel-1_Greenland_Ice_Velocity/issues) and use the 
word "tutorial" in the issue title.
