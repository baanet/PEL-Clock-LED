# Version 20250617 @ 17:45
# The program checks the file 'mod data' and updates the relevant version.json file

import os
import time

def update_version_data(file_path):
    statinfo = os.stat(file_path) # Get file details [8] is the mod date
    mod_date = statinfo[8]
    mod_date_info = time.localtime(mod_date)

    # Get year
    mod_date_year = str(mod_date_info[0]) 

    # Get and Fix month
    if mod_date_info[1]  < 10:
        mod_date_month = "0" + str(mod_date_info[1])
    else:
        mod_date_month = str(mod_date_info[1])

    # Get and Fix day
    if mod_date_info[2]  < 10:
        mod_date_day = "0" + str(mod_date_info[2])
    else:
        mod_date_day = str(mod_date_info[2])

    mod_date_data = mod_date_year + mod_date_month + mod_date_day # Reformatted date to year/month/day e.g.20250617

    file_path = file_path.rstrip('.py') # strip file suffix i.e. '.py'

    # Create version file
    version_file = "version.json." + file_path
    print('Updated: ' + version_file)
    version = '{"version": ' + mod_date_data + '}'
    fota = open(version_file, 'w')
    fota.write(version)
    fota.close

update_version_data('boot.py')

update_version_data('main.py')

update_version_data('file_mod_ota.py')

update_version_data('start_up_check.py')

print('\nUpdated all version files')
