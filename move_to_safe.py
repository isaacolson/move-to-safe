#!/usr/bin/env python
"""Move To Safe Farmware"""

from farmware_tools import device

device.log('starting!', 'success', ['toast'])

pos_x = device.get_current_position('x')
pos_y = device.get_current_position('y')
pos_z = z_height

device.move_absolute(pos_x, pos_y, pos_z)

device.log('ending!', 'success', ['toast'])


if __name__ == '__main__':
    farmware_name = 'move_to_safe'
    # Load inputs from Farmware page widget specified in manifest file
    z_height = get_env('safe_z')
