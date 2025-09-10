# inputs
path_archive = '/gws/ssde/j25b/cpom/aduffey/pp_archive_hills/'
UKESM_ARISE_run_IDs = ['cl322', 'cl458', 'cl459', 'cl460', 'cl461']
UKESM_ARISE_run_dict = {'cl322':'r1i1p1f2', 'cl458':'r2i1p1f2', 'cl459':'r3i1p1f2',
                        'cl460':'r4i1p1f2', 'cl461':'r8i1p1f2'}
ens_mems_arise_UK = ['r1i1p1f2', 'r2i1p1f2', 'r3i1p1f2', 'r4i1p1f2', 'r8i1p1f2']
CESM_ARISE_run_IDs = ['001', '002', '003', '004', '005'] # note there ten members, but we use only 5 here to align UKESM
ens_mems_CE = ['r1i1p1f1', 'r2i1p1f1', 'r3i1p1f1', 'r4i1p1f1', 'r5i1p1f1']
UKESM_arise_inj_logs_path = '../../Extra_data/ARISE_injection_stats/UKESM_feedback_stats/'
CESM_arise_inj_logs_path = '../../Extra_data/ARISE_injection_stats/CESM_feedback_stats/'
HiLLA_inj_mag = 12 # Tg per year total (6Tg per hemisphere)

ens_mems_UK_ssp245_all = ['r10i1p1f2','r11i1p1f2','r12i1p1f2','r16i1p1f2',
                          'r17i1p1f2','r18i1p1f2','r19i1p1f2','r1i1p1f2',
                          'r2i1p1f2','r3i1p1f2','r4i1p1f2','r5i1p1f2',
                          'r6i1p1f2','r7i1p1f2','r8i1p1f2','r9i1p1f2']

### Settings
colours = {'ssp245':'gray',
           'ssp245_light':'lightgray',
           'HiLLA_13':'red',
           'HiLLA_15':'green',
           'ARISE':'purple'}

model_colors = {'UKESM':'salmon',
                'CESM':'lightskyblue',
                'E3SM':'seagreen'}

dark_model_colors = {'UKESM':'orangered',
                     'CESM':'deepskyblue',
                     'E3SM':'seagreen'}

models = ['UKESM', 'CESM', 'E3SM']
model_names = {'UKESM':'UKESM1', 'CESM':'CESM2-WACCM', 'E3SM':'E3SMv3'}

HiLLA_altitudes = ['13km', '15km']

assessment_period = [2050, 2069]

lat_band_dict = {'Tropics':[-23, 23], 
                 'Arctic':[66, 91],
                 'Antarctic':[-91, -66],
                 'Global':[-91, 91],
                 'NH':[0, 91],
                 'SH':[-91, 0]}

regions = ['Global', 'Arctic', 'Tropics', 'NH', 'SH', 'Antarctic']