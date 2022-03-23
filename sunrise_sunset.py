#!/usr/bin/env python3

"""Demonstration of using multiple external Python packages to write a short
program to calculate sunrise and sunset time."""

import sys
from datetime import date, timedelta
from geopy.geocoders import Nominatim
from dateutil import tz
from skyfield import api
from skyfield import almanac


def main():
    """Main function"""
    if len(sys.argv) < 3:
        print('Please provide an address and date.')
        print('For example:')
        print(
            f'{sys.argv[0]} "800 N State College Blvd, Fullerton, CA 92831" 2022-03-18'
        )
        sys.exit(1)
    else:
        address = sys.argv[1]
        try:
            target_date = date.fromisoformat(sys.argv[2])
        except ValueError:
            print('Please use dashes when specifying a date.')
            sys.exit(1)
        print(f'The address you provided is {address}')
        print(f'The date you provided is {target_date}')
    location = Nominatim(user_agent="CSUF CPSC 386 Pip Demo").geocode(address)
    ts = api.load.timescale()
    eph = api.load('de421.bsp')
    spot = api.wgs84.latlon(location.latitude, location.longitude)
    tomorrow = target_date + timedelta(days=1)
    events = (
        ts.utc(target_date.year, target_date.month, target_date.day, 4),
        ts.utc(tomorrow.year, tomorrow.month, tomorrow.day, 4),
    )
    times, event_status = almanac.find_discrete(
        events[0], events[1], almanac.sunrise_sunset(eph, spot)
    )
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    for time, status in zip(times.utc_datetime(), event_status):
        local_time = time.replace(tzinfo=from_zone).astimezone(to_zone)
        if status:
            print('The sun will rise at ', end='')
        else:
            print('The sun will set at ', end='')
        print(local_time)


if __name__ == '__main__':
    main()
