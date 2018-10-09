#!/usr/bin/env python
"""Move To Safe Farmware"""

from farmware_tools import device

import os
import json
import base64
import math
import requests

pos_x = device.get_current_position('x')
pos_y = device.get_current_position('y')
pos_z = device.get_current_position('z')

device.move_absolute(pos_x, pos_y, pos_z)

if __name__ == '__main__':
    farmware_name = 'move_to_safe'
    # Load inputs from Farmware page widget specified in manifest file
    z_pos = get_env('safe_z')
