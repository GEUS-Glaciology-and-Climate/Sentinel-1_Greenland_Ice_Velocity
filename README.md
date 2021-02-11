# Sentinel-1_Greenland_Ice_Velocity

## Product info:
The PROMICE Ice Velocity product is a timeseries of Greenland Ice Sheet velocity mosaics based on ESA Sentinel-1 SAR offset tracking. 
+ The product span the period September 2016 to present. 
+ Spatial resolution: 500 m
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
+ The PROMICE Ice Velocity dataset for Greenland is available at: https://dataverse01.geus.dk/dataverse/Ice_velocity/ 
+ I want all the data wihout clicking on each file! How do I do that? 
  + Use `wget`
  + Use the script posted further up for bulk dowload.

## How to cite:
