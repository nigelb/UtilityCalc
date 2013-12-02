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

import json
import argparse
from utilitycalc.config import UtilityConfig

__description = "utility-calc will calculate the shares each person should pay on a utility bill"


def parse_cmdline():
    parser = argparse.ArgumentParser(description=__description)
    parser.add_argument("input", help='The json formatted input file.')
    return parser.parse_args()


def calculate():
    args = parse_cmdline()
    with open(args.input, "rb") as calc_config:
        config_data = json.load(calc_config)
    config = UtilityConfig(config_data)
    price_per_person_per_day = config_data['total'] / config.get_people_days()

    print "%s: " % config_data['name']
    print ""
    print "\t Start Date              : %s" % config.startDate.__str__()
    print "\t End Date                : %s" % config.endDate.__str__()
    print "\t Bill Total              : %s" % config_data['total']
    print "\t Person Days             : %s" % config.get_people_days()
    print "\t Price per person per day: %s" % price_per_person_per_day

    print ""
    print "\t Shares: "
    print ""
    rounded_total = 0
    for i in config.shares:
        share = round((config.shares[i]['days'] * price_per_person_per_day), 0)
        rounded_total += share
        print "\t\t %s:" % i
        print "\t\t\t Start Date: %s" % config.shares[i]['startDate'].__str__()
        print "\t\t\t End Date  : %s" % config.shares[i]['startDate'].__str__()
        print "\t\t\t Days      : %s" % config.shares[i]['days']
        print "\t\t\t Share     : $%s" % share
        print ""
    print ""
    print "Rounded total: ", rounded_total