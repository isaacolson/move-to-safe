#!/usr/bin/env python
"""Move To Safe Farmware"""

from farmware_tools import device
from farmware_tools import get_config_value

# Load inputs from Farmware page widget specified in manifest file
z_height = get_config_value('Move To Safe', 'safe_z')

pos_x = device.get_current_position('x')
pos_y = device.get_current_position('y')
pos_z = z_height

device.log('Moving to ' + str(pos_x) + ', ' + str(pos_y) + ', ' + str(pos_z), 'success', ['toast'])

device.move_absolute(
    {'x': int(pos_x), 
     'y': int(pos_y), 
     'z': int(pos_z)
    }, 100,
    {'x': 0, 
     'y': 0, 
     'z': 0
    })

device.log('ending!', 'success', ['toast'])

if __name__ == '__main__':
    farmware_name = 'move_to_safe'
