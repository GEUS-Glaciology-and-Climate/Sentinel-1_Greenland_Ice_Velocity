# Sentinel-1_Greenland_Ice_Velocity

## Product info:
The PROMICE Ice Velocity product is a timeseries of Greenland Ice Sheet velocity mosaics based on ESA Sentinel-1 SAR offset tracking. 
+ The product span the period January 2016 to present. 
+ Spatial resolution: 200 m
+ Temporal resolution: 12 days
+ Each mosaic span 2 Sentinel-1A cycles i.e. 24 days. All possible 6 and 12 day pairs using Sentinel-1A and 1B is included in the mosaic. 
+ A new mosaic is available approximately every 12 days. We aim to make it available within 10 days of the last included acquisition.

## Product data format:
+ Each mosaic is supplied as a NetCDF file.
+ Projection: Polar Stereographic projection (EPSG 3413). 
  + Latitude of true scale: 70<sup>o</sup>N.
  + Reference longitude: 45<sup>o</sup>W.
+ File content:

| Variable                       | Description                                      |Unit                    | 
| -------------                  | -------------                                    |----                    |
| x                              | x-coordinate of projection                       | m                      | 
| y                              | y-coordinate of projection                       | m                      |
| time                           | Midpoint time of all contributing acquisitions   | Days since 1990-1-1    |
| time_bnds                      | First and last time of contributing acquisitions | Days since 1990-1-1    |
| land_ice_surface_easting       | Ice velocity along x-axis                        | m/d                    |
| land_ice_surface_northing      | Ice velocity along y-axis                        | m/d                    |
| land_ice_surface_vertical      | Vertical velocity from surface parallel flow     | m/d                    |
| land_ice_surface_magnitude     | Horizontal ice velocity magnitude                | m/d                    |
| land_ice_surface_easting_std   | Ice velocity error estimate along x-axis         | m/d                    |
| land_ice_surface_northing_std  | Ice velocity error estimate along y-axis         | m/d                    |
| land_ice_surface_magnitude_std | Horizontal ice velocity error estimate           | m/d                    |

## How do I get the data? 
+ The PROMICE Ice Velocity dataset for Greenland is available at: https://dataverse.geus.dk/dataverse/Ice_velocity/ . All editions are available here.
+ I want all the data without clicking on each file! How do I do that? See info on the dataverse page.

## How to cite:
+ When using the dataset please use: Anne Solgaard; Anders Kusk, 2021, "Greenland Ice Velocity from Sentinel-1 Edition 4", https://doi.org/10.22008/promice/data/sentinel1icevelocity/greenlandicesheet, GEUS Dataverse
+ Literature citation: Solgaard, A., Kusk, A., Merryman Boncori, J. P., Dall, J., Mankoff, K. D., Ahlstrøm, A. P., Andersen, S. B., Citterio, M., Karlsson, N. B., Kjeldsen, K. K., Korsgaard, N. J., Larsen, S. H., and Fausto, R. S.: Greenland ice velocity maps from the PROMICE project, Earth Syst. Sci. Data, 13, 3491–3512, https://doi.org/10.5194/essd-13-3491-2021, 2021.
+ Please add the following to your acknowledgements: "Ice velocity maps were produced as part of the
Programme for Monitoring of the Greenland Ice Sheet (PROMICE) using
Copernicus Sentinel-1 SAR images distributed by ESA, and were provided by the
Geological Survey of Denmark and Greenland (GEUS) at http://www.promice.dk."
