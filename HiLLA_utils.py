import os
import glob
import pandas as pd
import numpy as np
import xarray as xr
from xmip.preprocessing import rename_cmip6
import matplotlib.path as mpath
import matplotlib.pyplot as plt
import cftime
import matplotlib
import warnings
import matplotlib.pyplot as plt
from Utils import get_ds_from_ceda

from config import lat_band_dict

def get_ds(run, var, table, zonal_mean=False):
    file = '/gws/ssde/j25b/cpom/aduffey/pp_archive_hills/{r}/{t}/{v}/{r}_{v}.nc'.format(r=run, t=table, v=var)
    ds = xr.open_dataset(file)
    if zonal_mean:
        ds = ds.mean(dim='longitude')
    return ds

def cut_incomplete_years(ds):
    final_year = np.max(ds.time.dt.year.values)
    ds_final_year = ds.sel(time=str(final_year))
    if not len(ds_final_year.time.dt.month.values) == 12:
        ds = ds.sel(time=slice(None, str(final_year-1)))
    return ds

def spatial_mean(ds, region, zonal_mean=False, var='tas'):
    ds_ts = ds.sel(latitude=slice(lat_band_dict[region][0], lat_band_dict[region][1]))[var]
    if not zonal_mean:
        ds_ts = ds_ts.mean(dim=['longitude'])
    weights = np.cos(np.deg2rad(ds_ts['latitude']))
    ds_ts_w = ds_ts.weighted(weights)
    ds_ts = ds_ts_w.mean(dim='latitude')
    return ds_ts.to_dataset(name=var)


def set_time_to_center_of_bounds(ds, time_bounds_name='time_bounds'):
    time_bounds = ds[time_bounds_name]
    time_midpoints = time_bounds.mean(dim=time_bounds.dims[-1])
    new_ds = ds.assign_coords(time=time_midpoints)
    return new_ds

def get_ssp245_ds(model, centre, variable, members, table='Amon', grid='gn'):
    ds_list = []
    for es in members:
        path = '/badc/cmip6/data/CMIP6/ScenarioMIP/{c}/{m}/ssp245/{e}/{t}/{v}/{g}/latest/'.format(
            c=centre, m=model, e=es, t=table,v=variable, g=grid)
        #files = os.listdir(path)
        ds = rename_cmip6(xr.open_mfdataset(path+'*.nc')).rename({'x':'longitude', 'y':'latitude'})
        ds_list.append(ds)
    
    DS = xr.concat(ds_list, dim='Ensemble_member')
    return DS

def get_slice_annual_mean(DS):
    DS = DS.sel(time=slice('2015', '2069'))
    return DS.groupby('time.year').mean('time').load()

def get_time_slice_mean(ds):
    time_slice = ds.sel(time=slice('2051', '2069'))
    mean_values = time_slice.mean(dim='time')
    return mean_values

def yearly_timeseries(ds, region):
    ds_ts = ds.sel(latitude=slice(lat_band_dict[region][0], lat_band_dict[region][1])).mean(dim=['longitude'])
    ds_ts_yearly = ds_ts.groupby('time.year').mean('time').load()
    weights = np.cos(np.deg2rad(ds_ts_yearly['latitude']))
    ds_ts_yearly = ds_ts_yearly.weighted(weights).mean(dim='latitude')
    return ds_ts_yearly