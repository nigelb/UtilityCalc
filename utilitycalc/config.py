#!/usr/bin/env python
#
# UtilityCalc is a tool to assist in calculating shares when splitting bills
# Copyright (C) 2013 NigelB
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from datetime import datetime


def createDate(date):
    return datetime(*[int(x) for x in date.split('-')])


class UtilityConfig:
    def __init__(self, config_data):
        self.startDate = createDate(config_data['startDate'])
        self.endDate = createDate(config_data['endDate'])
        self.shares = {}
        self.people_days = 0
        self.billing_days = (self.endDate - self.startDate).days
        for i in config_data['shares']:
            self.shares[i] = share = {}
            if 'endDate' in config_data['shares'][i]:
                share['endDate'] = createDate(config_data['shares'][i]['endDate'])
            else:
                share['endDate'] = self.endDate

            if 'startDate' in config_data['shares'][i]:
                share['startDate'] = createDate(config_data['shares'][i]['startDate'])
            else:
                share['startDate'] = self.startDate
            share['days'] = (share['endDate'] - share['startDate']).days
            self.people_days += share['days']

    def get_people_days(self):
        return self.people_days
