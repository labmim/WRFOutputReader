#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 17:20:50 2016

@author: eowfenth
"""

import datetime
import time
import arrow


utc = arrow.utcnow()
print(utc)


print(utc.replace(hours=-1))

local = utc.to('America/Bahia')

print(local.humanize())